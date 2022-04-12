import tkinter as tk

from pages.ClockPage import ClockPage
from pages.TextSliderPage import TextSliderPage
from pages.WebOfferNotifier import WebOfferNotifier
from pages.WebOfferNotifierTwo import WebOfferNotifierTwo


class MainView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        clockPage = ClockPage(self)
        textSliderPage = TextSliderPage(self)
        webOfferNotifier = WebOfferNotifier(self)
        webOfferNotifierTwo = WebOfferNotifierTwo(self)

        buttonframe = tk.Frame(self, background='black',)
        container = tk.Frame(self)

        buttonframe.pack(side="bottom", fill="x", expand=False, )
        container.pack(side="top", fill="both", expand=True)

        clockPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        textSliderPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        webOfferNotifier.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        webOfferNotifierTwo.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Clock", command=clockPage.show)
        b2 = tk.Button(buttonframe, text="48 Laws of Power", command=textSliderPage.show)
        b3 = tk.Button(buttonframe, text="Offer Notifier", command=webOfferNotifier.show)
        b4 = tk.Button(buttonframe, text="Offer Notifier2", command=webOfferNotifierTwo.show)
        exit = tk.Button(buttonframe, text="Exit", command=quit)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        exit.pack(side="right")

        clockPage.show()
