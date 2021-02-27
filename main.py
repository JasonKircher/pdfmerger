import os, Gui, PdfParser
from tkinter import*

global_paths = []
global_entryPath = ""
global_exitPath = ""


def path_app(in_out):

    def elements():
        global global_entryPath
        global global_exitPath
        path_app.geometry("300x130")
        Gui.button(path_app, 'Done', 10, done).place(x=160, y=50, width=80, height=30)
        Gui.button(path_app, 'Desktop', 10, desktop).place(x=25, y=50, width=80, height=30)
        Gui.label(path_app, 'path:', ('bold', 14), 20, 10).place(x=25, y=10, width=70, height=20)
        Gui.label(path_app, 'current input:   ', ('', 7), 20, 10).place(x=20, y=80, width=80, height=30)
        Gui.label(path_app, global_entryPath, ('', 7), 20, 10).place(x=100, y=80, width=180, height=30)
        Gui.label(path_app, 'current output: ', ('', 7), 20, 10).place(x=20, y=100, width=80, height=30)
        Gui.label(path_app, global_exitPath, ('', 7), 20, 10).place(x=100, y=100, width=180, height=30)

    def desktop():
        global global_entryPath
        global global_exitPath
        if in_out == "in":
            global_entryPath = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
        elif in_out == "out":
            global_exitPath = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
        Gui.window_vis(path_app, -1)
        Gui.kys(path_app)

    def done():
        global global_entryPath
        global global_exitPath
        if text.get() != "":
            temp = text.get()
        else:
            temp = ""
        if in_out == "in":
            global_entryPath = temp
        elif in_out == "out":
            global_exitPath = temp
        Gui.window_vis(path_app, -1)
        Gui.kys(path_app)

    def func_path(event):
        done()

    path_app = Gui.new_window("enter a path", "300x150")
    elements()
    text = Gui.text_field(path_app, StringVar(path_app))
    text.place(x=130, y=10, width=140, height=20)
    Gui.window_vis(path_app, 1)
    Gui.key_bind(path_app, '<Return>', func_path)
    Gui.loop(path_app, 1)


def main_app():
    global global_entryPath
    global global_exitPath
    display_str = ""

    def elements():
        Gui.button(main_app, 'submit', 15, submit).grid(row=0, column=2, padx=00)
        Gui.button(main_app, 'MERGE', 15, end_me).grid(row=5, column=2, pady=20)
        Gui.button(main_app, 'clear', 10, clear).grid(row=5, column=0)
        Gui.button(main_app, 'set input path', 15, set_input_path).grid(row=5, column=1, pady=20)
        Gui.button(main_app, 'set output path', 15, set_output_path).grid(row=4, column=2, pady=20)
        Gui.label(main_app, 'filename:', ('bold', 14), 10, 10).grid(row=0, column=0)
        Gui.label(main_app,'exitfile-name:', ('bold', 14), 10, 10).grid(row=4, column=0)

    def start_path_app(path):
        if path == "in":
            path_app("in")
        elif path == "out":
            path_app("out")

    def print_str():
        nonlocal display_str
        global global_entryPath
        global global_exitPath
        pdf = "Give file names without .pdf "
        if global_entryPath == "":
            display_str = "Notice: Files must be in same directory as application. " + pdf
        else:
            display_str = "Notice: Files must be in " + global_entryPath + ". " + pdf

    def submit():
        global_paths.append(global_entryPath + text_top.get() + ".pdf")
        parts_list.insert("end", text_top.get())
        text_top.set('')

    def end_me():
        PdfParser.merge_pdf(global_paths, text_bot.get(), global_exitPath)
        parts_list.delete("1", "end")
        global_paths.clear()
        text_bot.set('')

    def clear():
        parts_list.delete("1", "end")
        global_paths.clear()

    def set_output_path():
        start_path_app("out")

    def set_input_path():
        start_path_app("in")
        print_str()
        parts_list.delete(0, 0)
        parts_list.insert(0, display_str)

    def func(event):
        if text_top.get() == "":
            return
        submit()

    main_app = Gui.new_window("PDF-Merger", "480x300")
    start_path_app("in")
    global_exitPath = global_entryPath
    print_str()
    Gui.window_vis(main_app, 0)
    elements()
    Gui.key_bind(main_app, '<Return>', func)

    text_top = Gui.text_field(main_app, StringVar(main_app))
    text_bot = Gui.text_field(main_app, StringVar(main_app))
    text_top.grid(row=0, column=1)
    text_bot.grid(row=4, column=1)

    parts_list = Listbox(main_app, height=8, width=75, border=0)
    parts_list.grid(row=2, column=0, columnspan=3, padx=10)
    parts_list.insert("end", display_str)

    Gui.loop(main_app, 0)


# stating program
main_app()
