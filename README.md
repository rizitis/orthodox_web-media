## Rewrite from scratch everything.<br>
*Old version look for in [branches](https://github.com/rizitis/orthodox_web-media/branches) or download [2024.7.1](https://github.com/rizitis/orthodox_web-media/releases)*<br>
Now we have only 2 new files here for testing, vlc1.py and mpv1.py <br> one use vlc and other mpv as media players.  
 <p>
 
 How to use/test it:
 ```
 python3 vlc1.py or mpv1.py
 ```
 
 If you feel brave command: `python3 vlc1.py & disown -a && exit`
 
<p>Everything looks ok for now but I m not python guy any patches welcome... 
 We are in testing mode
 
 
 
 
 
 
 
 
 
 
 
 Requires:<br>
 
 


```import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QDesktopServices  # Import QDesktopServices from PyQt5.QtGui
from PyQt5.QtCore import QUrl
