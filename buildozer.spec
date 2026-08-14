[app]
title = JARVIS
package.name = jarvis
package.domain = com.jarvis.app
source.dir =.
version = 0.1
requirements = python3,kivy==2.3.0

[buildozer]
log_level = 2

[app:android]
p4a.bootstrap = sdl2
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 37.0.0
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
