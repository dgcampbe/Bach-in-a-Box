#!/usr/bin/env python
"""Main."""
import music21
import composition
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtCore import QFile
import interface


class MainWindow(QMainWindow):
    """Main window."""

    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = interface.Ui_window()
        self.ui.setupUi(self)


def main():
    """Main."""
    voice = composition.Voice("test", music21.scale.MajorScale("D"),
                              12, "tenor")
    voice.compose()
    print(str(voice))
    # Run interface
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
