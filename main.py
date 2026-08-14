from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class JarvisLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text='JARVIS FUNCIONANDO', font_size=30))
        btn = Button(text='Probar', size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: print("JARVIS OK"))
        self.add_widget(btn)

class JarvisApp(App):
    def build(self):
        return JarvisLayout()

JarvisApp().run()
