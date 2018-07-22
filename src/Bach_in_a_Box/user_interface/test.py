#import PyQt5 as pyqt
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle("Bach in a Box")

window.show()
sys.exit(app.exec_())
