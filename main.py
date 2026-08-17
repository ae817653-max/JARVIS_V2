from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

from jnius import autoclass, PythonJavaClass, java_method


# Android
PythonActivity = autoclass("org.kivy.android.PythonActivity")
Intent = autoclass("android.content.Intent")
RecognizerIntent = autoclass("android.speech.RecognizerIntent")
Toast = autoclass("android.widget.Toast")
String = autoclass("java.lang.String")


class SpeechListener(PythonJavaClass):
    __javainterfaces__ = ["android/speech/RecognitionListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Landroid/os/Bundle;)V")
    def onReadyForSpeech(self, params):
        pass

    @java_method("()V")
    def onBeginningOfSpeech(self):
        pass

    @java_method("([B)V")
    def onBufferReceived(self, buffer):
        pass

    @java_method("()V")
    def onEndOfSpeech(self):
        pass

    @java_method("(I)V")
    def onError(self, error):
        self.callback("")

    @java_method("(Landroid/os/Bundle;)V")
    def onResults(self, results):
        try:
            matches = results.getStringArrayList(
                RecognizerIntent.EXTRA_RESULTS
            )

            if matches and matches.size() > 0:
                texto = str(matches.get(0))
                self.callback(texto)
            else:
                self.callback("")
        except Exception:
            self.callback("")

    @java_method("(Landroid/os/Bundle;)V")
    def onPartialResults(self, partialResults):
        pass

    @java_method("(I[F)V")
    def onRmsChanged(self, rmsdB, values):
        pass

    @java_method("(Landroid/os/Bundle;)V")
    def onEvent(self, eventType, params):
        pass


class JarvisLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=30,
            spacing=20,
            **kwargs
        )

        self.estado = Label(
            text="JARVIS listo",
            font_size="24sp"
        )

        self.resultado = Label(
            text="Pulsa ESCUCHAR para hablar",
            font_size="20sp"
        )

        self.boton = Button(
            text="ESCUCHAR",
            font_size="22sp",
            size_hint_y=None,
            height=70
        )

        self.boton.bind(on_press=self.escuchar)

        self.add_widget(self.estado)
        self.add_widget(self.resultado)
        self.add_widget(self.boton)

        self.reconocedor = None
        self.escuchando = False

    def hablar(self, texto):
        try:
            TextToSpeech = autoclass(
                "android.speech.tts.TextToSpeech"
            )
            Locale = autoclass("java.util.Locale")

            activity = PythonActivity.mActivity

            def inicializado(status):
                try:
                    if status == TextToSpeech.SUCCESS:
                        tts.setLanguage(Locale("es", "MX"))
                        tts.speak(
                            texto,
                            TextToSpeech.QUEUE_FLUSH,
                            None,
                            "JARVIS"
                        )
                except Exception:
                    pass

            tts = TextToSpeech(activity, inicializado)

        except Exception:
            pass

    def escuchar(self, *args):
        if self.escuchando:
            return

        self.escuchando = True
        self.estado.text = "JARVIS está escuchando..."
        self.boton.text = "ESCUCHANDO..."

        try:
            activity = PythonActivity.mActivity

            intent = Intent(
                RecognizerIntent.ACTION_RECOGNIZE_SPEECH
            )

            intent.putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )

            intent.putExtra(
                RecognizerIntent.EXTRA_LANGUAGE,
                "es-MX"
            )

            intent.putExtra(
                RecognizerIntent.EXTRA_MAX_RESULTS,
                1
            )

            self.reconocedor = SpeechListener(
                self.procesar_texto
            )

            activity.startActivityForResult(
                intent,
                1001
            )

            # Android devuelve el resultado mediante la actividad.
            # El botón queda bloqueado mientras se procesa.
            Clock.schedule_once(
                lambda dt: self.finalizar_escucha(),
                8
            )

        except Exception as e:
            self.resultado.text = "Error al iniciar el micrófono"
            self.finalizar_escucha()

    def procesar_texto(self, texto):
        texto = texto.strip().lower()

        if not texto:
            self.resultado.text = "No entendí."
            self.finalizar_escucha()
            return

        self.resultado.text = "Escuché: " + texto

        if any(
            palabra in texto
            for palabra in [
                "descansa",
                "salir",
                "apagar",
                "detente",
                "detener"
            ]
        ):
            self.estado.text = "JARVIS descansando"
            self.boton.text = "ESCUCHAR"
            self.escuchando = False
            self.hablar("Entendido. Descansaré.")
            return

        if "qué hora es" in texto or "que hora es" in texto:
            from datetime import datetime

            hora = datetime.now().strftime("%H:%M")
            respuesta = "Son las " + hora

            self.estado.text = "JARVIS respondió"
            self.hablar(respuesta)

        elif "hola" in texto:
            self.estado.text = "JARVIS respondió"
            self.hablar("Hola. ¿En qué puedo ayudarte?")

        else:
            self.estado.text = "Comando recibido"
            self.hablar(
                "Escuché " + texto
            )

        self.finalizar_escucha()

    def finalizar_escucha(self):
        self.escuchando = False
        self.boton.text = "ESCUCHAR"


class JarvisApp(App):

    def build(self):
        self.title = "JARVIS"
        return JarvisLayout()


if __name__ == "__main__":
    JarvisApp().run()
