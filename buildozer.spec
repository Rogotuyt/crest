[app]

title = Crest
package.name = crest
package.domain = org.rogotuyt
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,pkl
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android settings
android.permissions =
android.api = 35
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Stable python-for-android release
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
