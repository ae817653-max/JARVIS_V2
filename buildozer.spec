[app]
title = JARVIS
package.name = jarvis
package.domain = com.jarvis.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[app:android]
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
