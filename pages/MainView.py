import tkinter as tk

from pages.ClockPage import ClockPage
from pages.TextSliderPage import TextSliderPage


class MainView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        clockPage = ClockPage(self)
        textSliderPage = TextSliderPage(self)

        buttonframe = tk.Frame(self, background='black',)
        container = tk.Frame(self)

        buttonframe.pack(side="bottom", fill="x", expand=False, )
        container.pack(side="top", fill="both", expand=True)

        clockPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        textSliderPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Clock", command=clockPage.show)
        b2 = tk.Button(buttonframe, text="48 Laws of Power", command=textSliderPage.show)
        exit = tk.Button(buttonframe, text="Exit", command=quit)

        b1.pack(side="left")
        b2.pack(side="left")
        exit.pack(side="right")

        clockPage.show()
