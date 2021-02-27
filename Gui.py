from tkinter import *


def new_window(title, dimension) -> Tk:
    app = Tk()
    app.title(title)
    app.geometry(dimension)
    # centering app
    y = (app.winfo_screenheight() - int(dimension.split("x")[1])) / 2 - 50
    x = (app.winfo_screenwidth() - int(dimension.split("x")[0])) / 2 - 50
    app.geometry("+%d+%d" % (x, y))
    app.resizable(width=None, height=None)
    return app


def window_vis(parent, duration):
    if duration == 1:
        parent.attributes("-topmost", True)
    elif duration == 0:
        parent.attributes("-topmost", True)
        parent.attributes("-topmost", False)
    elif duration == -1:
        parent.attributes("-topmost", False)


def kys(parent):
    parent.quit()
    parent.destroy()


def button(parent, name, width, func) -> Button:
    return Button(parent, text=name, width=width, command=func)


def label(parent, name, font, padx, pady) -> Label:
    return Label(parent, text=name, font=font, padx=padx, pady=pady)


def text_field(parent, text_variable):
    return Entry(parent, textvariable=text_variable)


def key_bind(parent, key, func):
    parent.bind(key, func)


def loop(parent, window_count):
    parent.mainloop(window_count)
