from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class mojaApka(App):   
        def build(self):
                plocha = BoxLayout(orientation="vertical")
                
                self.popisok = Label(text="ZATIAL NIC")
                plocha.add_widget(self.popisok)

                tlačidlo = Button(text="klikni ma")
                tlačidlo.bind(on_press=self.klik)
                plocha.add_widget(tlačidlo)

                return plocha

        def klik(self, kto_zavolal):
            self.popisok.text = "klikol si"

mojaApka().run()
