from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 

class app_03_01(App):
    def build(self):
        koren = BoxLayout()
        koren.add_widget (Label(text="ahoj"))
        koren.add_widget (Button(text="klik"))
        return koren 
    
app_03_01().run()
