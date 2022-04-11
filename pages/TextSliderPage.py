from tkinter import *

from pages.Page import Page


class TextSliderPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.canvas = Canvas(self, bg='black', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(fill=BOTH, expand=1)
        text_var = """
        Prawo 1 Nigdy nie przyćmiewaj Mistrza!\t\t Prawo 2 Nigdy nie ufaj zbytnio przyjaciołom, naucz się używać wrogów\t\t Prawo 3 Zachowaj w tajemnicy twoje intencje\t\t Prawo 4 Zawsze mów mniej niż potrzeba\t\t Prawo 5 Tak wiele zależy od reputacji. Strzeż jej za wszelką cenę\t\t Prawo 6 Za wszelką cenę zwracaj na siebie uwagę\t\t Prawo 7 Spraw, żeby inni pracowali za ciebie, ale to ty zbierz laury\t\t Prawo 8 Spraw, by inni do ciebie przychodzili, użyj zaczepki, jeśli trzeba\t\t Prawo 9 Wygrywaj działaniem, nigdy przekonywaniem\t\t Prawo 10 Zaraźliwość: unikaj nieszczęśliwych i pechowców\t\t Prawo 11 Naucz się utrzymywać innych w zależności od ciebie\t\t Prawo 12 Stosuj wybiórczo uczciwość i hojność, żeby rozbroić swoją ofiarę\t\t Prawo 13 Kiedy prosisz o pomoc, odwołuj się do własnego interesu ludzi, nigdy nie licz na łaskę lub wdzięczność\t\t Prawo 14 Udawaj przyjaciela, pracuj jak szpieg\t\t Prawo 15 Kompletnie zniszcz swojego wroga\t\t Prawo 16 Stosuj nieobecność, żeby zyskać większy szacunek\t\t Prawo 17 Trzymaj innych w napięciu: kultywuj atmosferę nieprzewidywalności\t\t Prawo 18 Nie buduj fortec, żeby się schronić. Izolacja jest niebezpieczna\t\t Prawo 19 Wiedz, z kim masz do czynienia. Nie obraź niewłaściwej osoby\t\t Prawo 20 Nie wtrącaj się w niczyje sprawy\t\t Prawo 21 Udawaj naiwnego, żeby złapać naiwnego. Wydawaj się głupszy niż twoja ofiara\t\t Prawo 22 Stosuj taktykę pokonanego: przekształć słabość w siłę\t\t Prawo 23 Skoncentruj swoje siły\t\t Prawo 24 Zachowuj się jak idealny dworzanin\t\t Prawo 25 Twórz siebie na nowo\t\t Prawo 26 Miej czyste ręce\t\t Prawo 27 Graj na ludzkiej potrzebie wierzenia, by stworzyć oddanych ślepo naśladowców\t\t Prawo 28 Brawurowo przystępuj do działania\t\t Prawo 29 Zaplanuj wszystko aż do końca\t\t Prawo 30 Niech innym wydaje się, że twoje osiągnięcia przychodzą ci łatwo\t\t Prawo 31 Kontroluj możliwości wyboru: niech inni grają kartami, które ty rozdasz\t\t Prawo 32 Graj na ludzkich fantazjach\t\t Prawo 33 Odkryj piętę achillesową każdego człowieka\t\t Prawo 34 Miej własny królewski styl: działaj jak król, aby traktowano cię jak króla\t\t Prawo 35 Zostań mistrzem działania w odpowiednim czasie\t\t Prawo 36 Lekceważ rzeczy, których nie możesz mieć: ignorowanie ich to najlepsza zemsta\t\t Prawo 37 Twórz ciekawe spektakle\t\t Prawo 38 Myśl co chcesz, ale zachowuj się jak inni\t\t Prawo 39 Zmąć wodę, by złowić rybę\t\t Prawo 40 Gardź darmowym obiadem\t\t Prawo 41 Unikaj udawania kogoś wielkiego\t\t Prawo 42 Uderz pasterza, a owce się rozproszą\t\t Prawo 43 Pracuj nad sercami i umysłami innych\t\t Prawo 44 Rozbrajaj i rozwścieczaj za pomocą efektu lustra\t\t Prawo 45 Głoś potrzebę zmiany, ale nigdy nie reformuj zbyt wiele naraz\t\t Prawo 46 Nigdy nie wydawaj się doskonały\t\t Prawo 47 Nie przekraczaj celu, do jakiego dążyłeś; gdy zwyciężysz, wiedz gdzie się zatrzymać\t\t Prawo 48 Przyjmij bezkształtną formę
        """
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
