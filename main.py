from kivy.app import App
from kivy.uix.widget import Widget
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Android WebView bindings via Pyjnius
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

class ZenInvoiceApp(App):
    def build(self):
        self.create_webview()
        return Widget()

    @run_on_ui_thread
    def create_webview(self):
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        
        # Configure settings for JavaScript, local storage, and file access
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowFileAccessFromFileURLs(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # Load your local HTML app from Android assets
        webview.loadUrl('file:///android_asset/index.html')
        
        activity.setContentView(webview)

if __name__ == '__main__':
    ZenInvoiceApp().run()
