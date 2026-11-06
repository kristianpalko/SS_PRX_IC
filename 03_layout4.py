from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 

class app_03_01(App):
     def build(self):
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="Nadpis", size_hint=(1, 0.5)))
        koren.add_widget(Button(text="Veľké tlačidlo"))            
        return koren 
       
       
app_03_01().run()
