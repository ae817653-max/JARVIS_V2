[app]
title = JARVIS V2.0
package.name = jarvisv2
package.domain = org.tu.jarvisv2
source.dir =.
version = 2.0
requirements = python3,kivy,android,Pyjnius,SpeechRecognition
orientation = portrait
services = JARVIS:service/main.py:sticky
android.permissions = RECORD_AUDIO,FOREGROUND_SERVICE,POST_NOTIFICATIONS,WAKE_LOCK,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
[buildozer]
log_level = 1
