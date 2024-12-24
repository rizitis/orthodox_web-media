import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

# Ορισμός των ραδιοσταθμών και των αντίστοιχων URLs
radio_stations = {
    'Radio: PemptousiaFM': 'https://stream.radiojar.com/48cz219puzzuv',
    'Radio: Μοναχική Διακονία': 'http://eco.onestreaming.com:8019/;stream.mp3&&duration=999999999999999999&id=scplayer&autostart=true',
    'Radio: Church of Piraeus': 'https://impradio2.bytemasters.gr/8002/stream',
    'Radio: Ι.Μ.Λεμεσού Κύπρος': 'http://194.154.128.242:9090/stream.mp3',
    'Radio: Μαρτυρία Χανιά': 'https://sc2.streamwithq.com:2000/stream/martiria',
    'Radio: Ιερα Μητρ. Χαλκίδος': 'http://65.108.133.10:8036/stream',
    'Radio: Ι. Μητρ. Πατρών': 'http://eco.onestreaming.com:8468/1fbbecaa-3eaa-11e9-aa55-52543be04c81',
    'Radio: Ορθοδοξία και Παράδοση': 'http://radio.lts-group.eu:52390/ANS',
    'Terirem Radio': 'https://c34.radioboss.fm:18213/stream',
    'TV: 3E': 'http://eu2.tv4e.gr:554/live/smil:myStream.sdp.smil/playlist.m3u8',
    'EcclesiaTV': 'https://liveopen.siliconweb.com/openTvLive/openEcclessia/playlist.m3u8',
    'PemptousiaTV': 'https://new.cache-stream.workers.dev/stream/UCYjyS5OIpeVoOoXRxpzaKDg/live.m3u8',
    # Add more ...using same format.
}

sites = {
    'Site: Pemptousia': 'https://www.pemptousia.gr',
    'Site: Orthodox News': 'https://www.orthodoxianewsagency.gr',
    'Site: ST. MAXIM THE GREEK INSTITUTE ': 'https://www.stmaximthegreek.org',
}

class RadioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.QMPlay2_processes = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Christian Orthodox web media')
        self.setGeometry(100, 100, 400, 300)

        # Κεντρική διάταξη
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Δημιουργία κεντρικού widget
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        self.layout.addWidget(central_widget)

        # Ρύθμιση του στυλ του παραθύρου
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;  /* Σκοτεινό φόντο */
                color: #f0f0f0;  /* Ελαφρύ κείμενο */
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background-color: #333333;  /* Σκοτεινό φόντο για κουμπιά */
                color: #ffffff;  /* Λευκό κείμενο */
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                margin: 5px;
                border: 1px solid #555555;  /* Προσθήκη περιγράμματος */
            }
            QPushButton:hover {
                background-color: #444444;  /* Αχνο χρώμα όταν περνάει το ποντίκι */
            }
            QPushButton:pressed {
                background-color: #555555;  /* Αχνό χρώμα όταν πατηθεί το κουμπί */
            }
            QLabel {
                color: #f0f0f0;
                font-size: 18px;
            }
        """)

        # Προσθήκη κουμπιών για κάθε ραδιοσταθμό
        for station, url in radio_stations.items():
            button = QPushButton(station, self)
            button.setFixedSize(300, 50)
            button.clicked.connect(lambda checked, url=url: self.play_station(url))
            central_layout.addWidget(button)

        # Προσθήκη κουμπιού για την ιστοσελίδα
        website_button = QPushButton('Site: Pemptousia', self)
        website_button.setFixedSize(300, 50)
        website_button.clicked.connect(lambda: self.open_website(sites['Site: Pemptousia']))
        central_layout.addWidget(website_button)
        website_button = QPushButton('Site: Orthodox News', self)
        website_button.setFixedSize(300, 50)
        website_button.clicked.connect(lambda: self.open_website(sites['Site: Orthodox News']))
        central_layout.addWidget(website_button)
        website_button = QPushButton('Site: ST. MAXIM THE GREEK INSTITUTE', self)
        website_button.setFixedSize(300, 50)
        website_button.clicked.connect(lambda: self.open_website(sites['Site: ST. MAXIM THE GREEK INSTITUTE']))
        central_layout.addWidget(website_button)

        video_button = QPushButton('Play Local Files', self)
        video_button.setFixedSize(300, 50)
        video_button.clicked.connect(self.open_video_file)
        central_layout.addWidget(video_button)

        # Κουμπί εξόδου
        exit_button = QPushButton('Έξοδος', self)
        exit_button.setFixedSize(300, 50)
        exit_button.clicked.connect(self.close)
        central_layout.addWidget(exit_button)

    def play_station(self, url):
        try:
            process = subprocess.Popen(['QMPlay2', url])
            self.QMPlay2_processes.append(process)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to play station: {e}")

    def open_video_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Επιλογή Αρχείου Βίντεο', '', 'Video Files (*.mp4 *.avi *.mov *.mkv)')
        if file_name:
            try:
                process = subprocess.Popen(['QMPlay2', file_name])
                self.QMPlay2_processes.append(process)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to play video: {e}")

    def open_website(self, url):
        try:
            QDesktopServices.openUrl(QUrl(url))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open website: {e}")

    def closeEvent(self, event):
        self.hide()  # Hide the window instead of closing it
        event.ignore()  # Ignore the close event so the window remains hidden

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadioApp()
    ex.show()
    sys.exit(app.exec_())
