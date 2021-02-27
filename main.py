import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *

global_paths = []
global_entryPath = ""
global_exitPath = ""
temp = ""


def start_main():
    mainapp()


def merge_pdf(input_paths, filename):
    global global_paths
    if filename == "":
        filename = "out"
    writer = PdfFileWriter()
    for i in input_paths:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(page))
    with open(global_exitPath + filename + ".pdf", "wb") as f_out:
        writer.write(f_out)


def split_pdf(path, num):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for page in range(num):
            writer = PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{page}.pdf", "wb") as f_out:
                writer.write(f_out)


def pathapp(in_out):
    global temp
    temp = in_out

    def desktop():
        global temp
        temp = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
        path_app.attributes("-topmost", False)
        path_app.quit()
        path_app.destroy()

    def done():
        global temp
        global global_entryPath
        if part_text_path.get() != "":
            temp = part_text_path.get()
        else:
            temp = ""
        path_app.attributes("-topmost", False)
        path_app.quit()
        path_app.destroy()

    def func_path(event):
        done()

    def path_app_size():
        global global_entryPath
        if (global_entryPath == "") & (global_exitPath == ""):
            path_app.geometry("300x100")
        else:
            path_app.geometry("300x130")
            t1 = Label(path_app, text='current input:   ', font=('', 7), padx=20, pady=10)
            t1.place(x=20, y=80, width=80, height=30)
            p1 = Label(path_app, text=global_entryPath, font=('', 7), padx=20, pady=10)
            p1.place(x=100, y=80, width=180, height=30)
            t2 = Label(path_app, text='current output: ', font=('', 7), padx=20, pady=10)
            t2.place(x=20, y=100, width=80, height=30)
            p2 = Label(path_app, text=global_exitPath, font=('', 7), padx=20, pady=10)
            p2.place(x=100, y=100, width=180, height=30)

    path_app = Tk()
    path_app.title("enter a path")
    path_app.geometry("300x100")
    path_app.wm_minsize(300, 100)
    path_app.wm_maxsize(300, 150)
    x = (path_app.winfo_screenwidth() - 300) / 2 - 50
    y = (path_app.winfo_screenheight() - 100) / 2 - 50
    path_app.geometry("+%d+%d" % (x, y))

    path_app_size()
    path_app.attributes("-topmost", True)

    part_text_path = StringVar(path_app)

    part_label_path = Label(path_app, text='path:', font=('bold', 14), padx=20, pady=10)
    part_label_path.place(x=25, y=10, width=70, height=20)

    part_entry_path = Entry(path_app, textvariable=part_text_path)
    part_entry_path.place(x=130, y=10, width=140, height=20)

    done_btn = Button(path_app, text='Done', width=10, command=done)
    done_btn.place(x=160, y=50, width=80, height=30)

    desktop_btn = Button(path_app, text='Desktop', width=10, command=desktop)
    desktop_btn.place(x=25, y=50, width=80, height=30)

    path_app.bind('<Return>', func_path)

    path_app.mainloop(1)


def exitpathapp():
    global global_exitPath
    global temp
    pathapp(global_exitPath)
    global_exitPath = temp


def inputpathapp():
    global global_entryPath
    global temp
    pathapp(global_entryPath)
    global_entryPath = temp


def mainapp():
    global global_entryPath
    global global_exitPath
    display_str = ""

    def start_path_app(path):
        if path == "entry":
            inputpathapp()
        elif path == "exit":
            exitpathapp()

    def printstr():
        nonlocal display_str
        global global_entryPath
        global global_exitPath
        pdf = "Give file names without .pdf "
        if global_entryPath == "":
            display_str = "Notice: Files must be in same directory as application. " + pdf
        else:
            display_str = "Notice: Files must be in " + global_entryPath + ". " + pdf

    def submit_item():
        global_paths.append(global_entryPath + part_text.get() + ".pdf")
        parts_list.insert("end", part_text.get())
        part_text.set('')

    def end_me():
        merge_pdf(global_paths, part_exit_text.get())
        parts_list.delete("1", "end")
        global_paths.clear()
        part_exit_text.set('')

    def clear():
        parts_list.delete("1", "end")
        global_paths.clear()

    def set_output_path():
        start_path_app("exit")

    def set_input_path():
        start_path_app("entry")
        printstr()
        parts_list.delete(0, 0)
        parts_list.insert(0, display_str)

    def func(event):
        if part_text.get() == "":
            return
        submit_item()

    def close():
        app.quit()
        app.destroy()

    app = Tk()
    app.title("PDF-merger")
    app.geometry("480x300")
    app.wm_maxsize(480, 300)
    app.wm_minsize(480, 300)
    x = (app.winfo_screenwidth() - 480) / 2 - 50
    y = (app.winfo_screenheight() - 300) / 2 - 50
    app.geometry("+%d+%d" % (x, y))

    inputpathapp()
    global_exitPath = global_entryPath = temp
    printstr()
    app.attributes("-topmost", True)
    app.attributes("-topmost", False)
    app.bind('<Return>', func)

    part_text = StringVar(app)
    part_label = Label(app, text='filename:', font=('bold', 14), padx=10, pady=10)
    part_label.grid(row=0, column=0)
    part_entry = Entry(app, textvariable=part_text)
    part_entry.grid(row=0, column=1)

    parts_list = Listbox(app, height=8, width=75, border=0)
    parts_list.grid(row=2, column=0, columnspan=3, padx=10)
    parts_list.insert("end", display_str)

    remove_btn = Button(app, text='clear', width=10, command=clear)
    remove_btn.grid(row=5, column=0)

    part_exit_text = StringVar(app)
    part_exit_entry = Entry(app, textvariable=part_exit_text)
    part_exit_entry.grid(row=4, column=1)
    part_exit = Label(app, text='exitfile-name:', font=('bold', 14), padx=10, pady=10)
    part_exit.grid(row=4, column=0)

    in_path_btn = Button(app, text='set input path', width=15, command=set_input_path)
    in_path_btn.grid(row=5, column=1, pady=20)

    out_path_btn = Button(app, text='set output path', width=15, command=set_output_path)
    out_path_btn.grid(row=4, column=2, pady=20)

    merge_btn = Button(app, text='MERGE', width=15, command=end_me)
    merge_btn.grid(row=5, column=2, pady=20)

    submit_btn = Button(app, text='submit', width=15, command=submit_item)
    submit_btn.grid(row=0, column=2, padx=00)

    app.mainloop()


# stating program
mainapp()
