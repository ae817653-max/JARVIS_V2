[app]
title = JARVIS V2
package.name = jarvisv2
package.domain = com.jarvis.v2
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
