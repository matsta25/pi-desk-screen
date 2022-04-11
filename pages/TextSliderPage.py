from tkinter import *

from pages.Page import Page


class TextSliderPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.canvas = Canvas(self, bg='black', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(fill=BOTH, expand=1)
        text_var = "Hello from text slider page!"
        self.canvas.create_text(0, -2000, text=text_var, font=('calibri', 20, 'bold'), fill='white',
                                tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = self.canvas.bbox("marquee")
        width = x2 - x1
        height = y2 - y1
        self.canvas['width'] = width
        self.canvas['height'] = height
        self.fps = 60
        self.shift()

    def shift(self):
        x1, y1, x2, y2 = self.canvas.bbox("marquee")
        if x2 < 0 or y1 < 0:  # reset the coordinates
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height() // 2
            self.canvas.coords("marquee", x1, y1)
        else:
            self.canvas.move("marquee", -2, 0)
        self.canvas.after(1000 // self.fps, self.shift)
