[app]

title = StreamSanctum
package.name = streamsanctum
package.domain = org.saden

source.dir = .
source.include_exts = py,html

version = 0.1
requirements = python3,kivy,flask,pyjnius

orientation = portrait
fullscreen = 0

# صلاحيات أندرويد
android.permissions = INTERNET

# إعدادات API
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# مكتبات إضافية
android.gradle_dependencies = androidx.webkit:webkit:1.4.0

# إعدادات أخرى
android.allow_backup = True
android.support = True
android.accept_sdk_license = True

# أيقونة وشاشة تحميل
# icon.filename = path/to/icon.png
# presplash.filename = path/to/presplash.png
