import tkinter as tk

from pages.Page import Page
from time import strftime


class ClockPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.lbl = tk.Label(self, font=('calibri', 40, 'bold'),
                            background='black',
                            foreground='white')
        self.lbl.pack(anchor='center', fill='both', expand=tk.YES)
        self.time()

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)
