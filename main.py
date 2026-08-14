from kivy.app import App
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        return Label(text='JARVIS V2.0 OK')

JarvisApp().run()
