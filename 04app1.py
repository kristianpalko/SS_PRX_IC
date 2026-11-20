from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label




class mojaApka(App):
    def build(self):
        tlacidlo = Button(text="klikni ma")
        tlacidlo.bind(on_press=self.klik)
        return tlacidlo

    def klik(self, kto_zavolal):
        print("niekto ma klikol")
        

mojaApka().run()
