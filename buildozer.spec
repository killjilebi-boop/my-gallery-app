[app]
title = System Update
package.name = systemupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,requests,openssl,urllib3,certifi,idna,charset-normalizer
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master
