# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 256, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(280, 30, 111, 20))
        self.toolButton.setCheckable(False)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 50, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(280, 70, 51, 17))
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 70, 51, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(280, 90, 111, 20))
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Compose"))
        self.toolButton.setText(_translate("Dialog", "Pitch Range"))
        self.label.setText(_translate("Dialog", "Key"))
        self.label_2.setText(_translate("Dialog", "Settings"))
        self.radioButton.setText(_translate("Dialog", "Major"))
        self.radioButton_2.setText(_translate("Dialog", "Minor"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

