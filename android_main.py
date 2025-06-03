from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform

if platform == 'android':
    from android import mActivity
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    import socket

    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    LinearLayout = autoclass('android.widget.LinearLayout')

class WebViewApp(App):
    def build(self):
        if platform == 'android':
            # تأجيل البناء لحين قبول الصلاحيات
            request_permissions([Permission.INTERNET], self.permission_callback)
            return Widget()
        else:
            from kivy.uix.label import Label
            return Label(text="يُشغل فقط على Android")

    def permission_callback(self, permissions, grants):
        # تحقق من منح الصلاحية
        if all(grants):
            self.load_webview()

    def load_webview(self):
        local_ip = socket.gethostbyname(socket.gethostname())
        url = f'http://{local_ip}:5000'

        webview = WebView(mActivity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl(url)

        layout = LinearLayout(mActivity)
        layout.setOrientation(1)
        layout.addView(webview)
        mActivity.setContentView(layout)

if __name__ == '__main__':
    WebViewApp().run()
