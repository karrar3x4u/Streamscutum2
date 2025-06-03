[app]

title = StreamSanctum
package.name = streamsanctum
package.domain = org.saden

source.dir = .
source.include_exts = py, html

version = 0.1
requirements = python3, kivy, flask, pyjnius

orientation = portrait
fullscreen = 0

# صلاحيات أندرويد
android.permissions = INTERNET
buildozer -v android debug

# API والمكتبات
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# WebView تعتمد على مكتبة خارجية
android.gradle_dependencies = androidx.webkit:webkit:1.4.0

# لدعم jnius و Java classes
android.available_builders = custom
android.private_storage = False

# دعم multi-threading إذا احتجت لاحقًا
android.allow_backup = True
android.support = True

# يقلل من مشاكل WebView وتحميلات الصفحات
android.add_jars = 

# عند ظهور مشاكل بـ aidl أو build-tools
android.accept_sdk_license = True

# منع buildozer من حذف ملفاتك
presplash.filename = 
icon.filename =
