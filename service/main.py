import time, speech_recognition as sr
from jnius import autoclass
Context = autoclass('android.content.Context')
Builder = autoclass('android.app.Notification$Builder')
Channel = autoclass('android.app.NotificationChannel')
Manager = autoclass('android.app.NotificationManager')
service = autoclass('org.kivy.android.PythonService').mService
m = service.getSystemService(Context.NOTIFICATION_SERVICE)
c = Channel('jarvis_channel', 'JARVIS', Manager.IMPORTANCE_LOW)
m.createNotificationChannel(c)
n = Builder(service, 'jarvis_channel')
n.setContentTitle('JARVIS Activo'); n.setContentText('Di descansa para apagar')
n.setSmallIcon(service.getApplicationInfo().icon); n.setOngoing(True)
service.startForeground(1, n.build())
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as s:
            r.adjust_for_ambient_noise(s, 0.5)
            a = r.listen(s, None, 4)
            cmd = r.recognize_google(a, language='es-MX').lower()
            if 'descansa' in cmd:
                service.stopForeground(True); service.stopSelf(); break
    except: time.sleep(1)
