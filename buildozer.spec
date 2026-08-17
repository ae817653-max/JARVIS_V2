[app]

# Nombre de la aplicación
title = JARVIS

# Nombre del paquete
package.name = jarvis

# Identificador único
package.domain = com.jarvis.app

# Carpeta donde está main.py
source.dir = .

# Archivos que se incluirán
source.include_exts = py,kv,png,jpg,jpeg,json,atlas

# Versión
version = 0.1

# Dependencias de Python
requirements = python3,kivy==2.3.0,pyjnius

# Orientación
orientation = portrait

# No iniciar en pantalla completa
fullscreen = 0


[buildozer]

# Registro de compilación
log_level = 2

# Advertencias de Buildozer
warn_on_root = 1


[android]

# Permiso para utilizar el micrófono
android.permissions = RECORD_AUDIO

# Permiso para acceder a Internet si posteriormente lo necesitamos
android.permissions = RECORD_AUDIO,INTERNET

# Arquitectura de Android
android.arch = arm64-v8a

# Versión mínima de Android
android.minapi = 23

# API objetivo
android.api = 35

# Nombre del APK
android.entrypoint = org.kivy.android.PythonActivity
