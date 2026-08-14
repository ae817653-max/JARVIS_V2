[app]
title = JARVIS
package.name = jarvis
package.domain = com.jarvis.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.ant_path = /usr/bin/ant
p4a.bootstrap = sdl2
p4a.branch = master
