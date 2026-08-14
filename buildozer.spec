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
warn_on_root = 0

[app:android]
p4a.bootstrap = sdl2
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 37.0.0
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
