import random
from tkinter import *

from pages.Page import Page


class TextSliderPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.rules = [
            "Prawo 1 Nigdy nie przyćmiewaj Mistrza!",
            "Prawo 2 Nigdy nie ufaj zbytnio przyjaciołom, naucz się używać wrogów",
            "Prawo 3 Zachowaj w tajemnicy twoje intencje",
            "Prawo 4 Zawsze mów mniej niż potrzeba",
            "Prawo 5 Tak wiele zależy od reputacji. Strzeż jej za wszelką cenę",
            "Prawo 6 Za wszelką cenę zwracaj na siebie uwagę",
            "Prawo 7 Spraw, żeby inni pracowali za ciebie, ale to ty zbierz laury",
            "Prawo 8 Spraw, by inni do ciebie przychodzili, użyj zaczepki, jeśli trzeba",
            "Prawo 9 Wygrywaj działaniem, nigdy przekonywaniem",
            "Prawo 10 Zaraźliwość: unikaj nieszczęśliwych i pechowców",
            "Prawo 11 Naucz się utrzymywać innych w zależności od ciebie",
            "Prawo 12 Stosuj wybiórczo uczciwość i hojność, żeby rozbroić swoją ofiarę",
            "Prawo 13 Kiedy prosisz o pomoc, odwołuj się do własnego interesu ludzi, nigdy nie licz na łaskę lub wdzięczność",
            "Prawo 14 Udawaj przyjaciela, pracuj jak szpieg",
            "Prawo 15 Kompletnie zniszcz swojego wroga",
            "Prawo 16 Stosuj nieobecność, żeby zyskać większy szacunek",
            "Prawo 17 Trzymaj innych w napięciu: kultywuj atmosferę nieprzewidywalności",
            "Prawo 18 Nie buduj fortec, żeby się schronić. Izolacja jest niebezpieczna",
            "Prawo 19 Wiedz, z kim masz do czynienia. Nie obraź niewłaściwej osoby",
            "Prawo 20 Nie wtrącaj się w niczyje sprawy",
            "Prawo 21 Udawaj naiwnego, żeby złapać naiwnego. Wydawaj się głupszy niż twoja ofiara",
            "Prawo 22 Stosuj taktykę pokonanego: przekształć słabość w siłę",
            "Prawo 23 Skoncentruj swoje siły",
            "Prawo 24 Zachowuj się jak idealny dworzanin",
            "Prawo 25 Twórz siebie na nowo",
            "Prawo 26 Miej czyste ręce",
            "Prawo 27 Graj na ludzkiej potrzebie wierzenia, by stworzyć oddanych ślepo naśladowców",
            "Prawo 28 Brawurowo przystępuj do działania",
            "Prawo 29 Zaplanuj wszystko aż do końca",
            "Prawo 30 Niech innym wydaje się, że twoje osiągnięcia przychodzą ci łatwo",
            "Prawo 31 Kontroluj możliwości wyboru: niech inni grają kartami, które ty rozdasz",
            "Prawo 32 Graj na ludzkich fantazjach",
            "Prawo 33 Odkryj piętę achillesową każdego człowieka",
            "Prawo 34 Miej własny królewski styl: działaj jak król, aby traktowano cię jak króla",
            "Prawo 35 Zostań mistrzem działania w odpowiednim czasie",
            "Prawo 36 Lekceważ rzeczy, których nie możesz mieć: ignorowanie ich to najlepsza zemsta",
            "Prawo 37 Twórz ciekawe spektakle",
            "Prawo 38 Myśl co chcesz, ale zachowuj się jak inni",
            "Prawo 39 Zmąć wodę, by złowić rybę",
            "Prawo 40 Gardź darmowym obiadem",
            "Prawo 41 Unikaj udawania kogoś wielkiego",
            "Prawo 42 Uderz pasterza, a owce się rozproszą",
            "Prawo 43 Pracuj nad sercami i umysłami innych",
            "Prawo 44 Rozbrajaj i rozwścieczaj za pomocą efektu lustra",
            "Prawo 45 Głoś potrzebę zmiany, ale nigdy nie reformuj zbyt wiele naraz",
            "Prawo 46 Nigdy nie wydawaj się doskonały",
            "Prawo 47 Nie przekraczaj celu, do jakiego dążyłeś; gdy zwyciężysz, wiedz gdzie się zatrzymać",
            "Prawo 48 Przyjmij bezkształtną formę"]

        self.canvas = Canvas(self, bg='black', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(fill=BOTH, expand=1)
        self.text_id = self.canvas.create_text(0, -2000, text=random.choice(self.rules), font=('calibri', 20, 'bold'), fill='white',
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
            self.canvas.itemconfig(self.text_id, text=random.choice(self.rules))
        else:
            self.canvas.move("marquee", -2, 0)
        self.canvas.after(1000 // self.fps, self.shift)
