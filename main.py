from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class JarvisApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20,
        )

        title = Label(
            text="JARVIS",
            font_size="32sp",
        )

        message = Label(
            text="Sistema iniciado correctamente",
            font_size="20sp",
        )

        button = Button(
            text="Probar JARVIS",
            size_hint_y=None,
            height=60,
        )

        def on_press(instance):
            message.text = "JARVIS está funcionando"

        button.bind(on_press=on_press)

        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(button)

        return layout


if __name__ == "__main__":
    JarvisApp().run()
