from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class mojaApka(App):   
        def build(self):
                plocha = BoxLayout(orientation="vertical")
                cast_in_out=boxlayout=BoxLayout()

                self.imput= TextInput(hint_text= 'zadaj cm')
                self.output= Label(text='')
                cast_in_out.add_widget(self.imput)
                cast_in_out.add_widget(self.output)

                plocha.add_widget(cast_in_out)
                return plocha

        def klik(self, kto_zavolal):
                pass




















mojaApka().run()

