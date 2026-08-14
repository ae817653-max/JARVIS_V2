from kivy.app import App
from kivy.uix.label import Label
class JarvisApp(App):
    def build(self):
        return Label(text="JARVIS V2 OK")
JarvisApp().run()
