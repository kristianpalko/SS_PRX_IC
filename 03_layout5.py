from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class app_03_01(App):
    def build(self):
        koren = BoxLayout(orientation="vertical")

        koren.add_widget(TextInput(hint_text="tu nieco napis"))

        tri_buttony = BoxLayout(orientation="horizontal")
        tri_buttony.add_widget(Button(text="A"))
        tri_buttony.add_widget(Button(text="B"))
        tri_buttony.add_widget(Button(text="C"))

        koren.add_widget(tri_buttony)

        return koren


app_03_01().run()