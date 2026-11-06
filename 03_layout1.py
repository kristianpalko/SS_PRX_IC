from kivy.app import App
from kivy.uix.button import Button

class app_03_01(App):
    def build(self):
        return Button(text = "klik",
                      font_size = 40)
    
    
    
    
    
app_03_01().run()