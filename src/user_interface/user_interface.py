from PyQt5 import QtCore, QtGui, QtWidgets
import bach_interface
import sys

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = bach_interface.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

main()
