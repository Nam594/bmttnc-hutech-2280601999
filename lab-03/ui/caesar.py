# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaesarCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CaesarCipher)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(170, 130, 321, 71))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(170, 220, 321, 21))
        self.txt_key.setObjectName("txt_key")
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(170, 310, 321, 71))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(170, 410, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(420, 420, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        CaesarCipher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaesarCipher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CaesarCipher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaesarCipher)
        self.statusbar.setObjectName("statusbar")
        CaesarCipher.setStatusBar(self.statusbar)

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "MainWindow"))
        self.label.setText(_translate("CaesarCipher", "Caesar Cipher"))
        self.label_2.setText(_translate("CaesarCipher", "Plain text"))
        self.label_3.setText(_translate("CaesarCipher", "Key"))
        self.label_4.setText(_translate("CaesarCipher", "Cipher Text"))
        self.btn_encrypt.setText(_translate("CaesarCipher", "Encrypt"))
        self.btn_decrypt.setText(_translate("CaesarCipher", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaesarCipher = QtWidgets.QMainWindow()
    ui = Ui_CaesarCipher()
    ui.setupUi(CaesarCipher)
    CaesarCipher.show()
    sys.exit(app.exec_())
