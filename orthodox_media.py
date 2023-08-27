import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QIcon
import subprocess 

class WebTVRadioApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web TV and Radio Player")
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.init_buttons()

    def init_buttons(self):
        icons_and_urls = {
            "/usr/share/orthodox_web-mediapem_tv.png": "https://svs.itworkscdn.net/pemptousialive/pemptousia.smil/playlist.m3u8",
            "/usr/share/orthodox_web-media/pem_fm.png": "https://stream.radiojar.com/48cz219puzzuv",
            "/usr/share/orthodox_web-media/imllogo.png": "http://194.154.128.242:9090/stream.mp3",
            "/usr/share/orthodox_web-media/4e.jpg": "http://eu2.tv4e.gr:554/live/smil:myStream.sdp.smil/playlist.m3u8"
        }

        for icon_path, url in icons_and_urls.items():
            pixmap = QPixmap(icon_path)
            pixmap = pixmap.scaled(100, 100)

            icon = QIcon(pixmap)

            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(pixmap.rect().size())
            button.clicked.connect(lambda checked, u=url: self.open_url(u))

            # Apply a custom stylesheet to the button
            button.setStyleSheet("background-color: #3498db; color: #ffffff; border: none; padding: 10px;")

            self.layout.addWidget(button)

    def open_url(self, url):
        subprocess.Popen(['vlc', url])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebTVRadioApp()
    window.show()
    sys.exit(app.exec_())
