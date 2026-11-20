from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label




class mojaApka(App):
    def build(self):
       
        plocha = BoxLayout(orientation="vertical")
       
                          
        return plocha

mojaApka().run()
