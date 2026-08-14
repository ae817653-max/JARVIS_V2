from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
from jnius import autoclass
PythonService = autoclass('org.kivy.android.PythonService')
mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
class JarvisApp(App):
    def build(self):
        request_permissions([Permission.RECORD_AUDIO, Permission.FOREGROUND_SERVICE, Permission.POST_NOTIFICATIONS])
        Intent = autoclass('android.content.Intent')
        intent = Intent(mActivity, PythonService)
        intent.setAction('org.kivy.android.PythonService')
        mActivity.startForegroundService(intent)
        return Label(text='JARVIS V2.0 ACTIVO')
JarvisApp().run()
