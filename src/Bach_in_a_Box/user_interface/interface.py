from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    
    import bach_interface

else:

    from user_interface import bach_interface

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = bach_interface.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    
    main()
