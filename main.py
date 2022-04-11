import tkinter as tk

import os

from pages.MainView import MainView

ENV = os.getenv('ENV')


def quit():
    global root
    root.quit()


class Main:
    def __init__(self):
        root = tk.Tk()
        main = MainView(root)
        main.pack(side="top", fill="both", expand=True)
        root.title("Pi Desk Screen")
        root.wm_geometry("480x320")
        root.configure(bg='black')
        if ENV != 'dev':
            root.attributes('-fullscreen', True)
            root.config(cursor="none")
        root.mainloop()


app = Main()
