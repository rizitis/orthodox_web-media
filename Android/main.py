from kivy.app import App
from kivy.utils import platform
from jnius import autoclass
import subprocess

class WebTVRadioApp(App):
    def build(self):
        # Replace the URL with the actual M3U8 stream URL
        media_url = "https://svs.itworkscdn.net/pemptousialive/pemptousia.smil/playlist.m3u8"

        if platform == 'android':
            # On Android, use Android intent to open the stream
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setDataAndType(Uri.parse(media_url), 'video/*')

            current_activity = PythonActivity.mActivity
            current_activity.startActivity(intent)
        else:
            # For other platforms, use subprocess to open the stream (VLC example)
            subprocess.Popen(['vlc', media_url])

if __name__ == "__main__":
    WebTVRadioApp().run()

