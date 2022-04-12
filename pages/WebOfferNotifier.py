import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk

from pages.Page import Page




class WebOfferNotifier(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_url = 'https://www.olx.pl/elektronika/q-brother/'
        self.pref_string_from_offer = ""


        self.lbl = tk.Label(self, font=('calibri', 13, 'bold'),
                            background='black',
                            foreground='white',
                            wraplength=300)
        self.lbl.pack(anchor='center', fill='both', expand=tk.YES)

        self.update_text()

    def update_text(self):
        self.lbl.config(foreground='white')
        new_string_from_offer = self.get_string_from_offer()
        if self.pref_string_from_offer != "" \
                and self.pref_string_from_offer != new_string_from_offer:
            self.lbl.config(foreground='red')
            self.pref_string_from_offer = new_string_from_offer
        self.lbl['text'] = new_string_from_offer
        self.lbl.after(1000, self.update_text)

    def get_string_from_offer(self):
        page = requests.get(self.page_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        newestNonPremiumOfferText = soup.find_all("div", {"class": "offer-wrapper"})[5].getText()
        text = os.linesep.join([s for s in newestNonPremiumOfferText.splitlines() if s])
        return text
