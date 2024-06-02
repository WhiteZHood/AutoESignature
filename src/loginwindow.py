from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from loginstorage import *
import storingfiles as sf

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("LoginWindow")
        self.resize(571, 396)

        self.loginwidget = QtWidgets.QWidget(self)
        self.loginwidget.setObjectName("loginwidget")

        self.labelUrlService = QtWidgets.QLabel(self.loginwidget)
        self.labelUrlService.setGeometry(QtCore.QRect(20, 50, 131, 41))
        self.labelUrlService.setObjectName("labelUrlService")
        
        self.labelPassword = QtWidgets.QLabel(self.loginwidget)
        self.labelPassword.setGeometry(QtCore.QRect(20, 140, 131, 41))
        self.labelPassword.setObjectName("labelPassword")

        self.loginButton = QtWidgets.QPushButton(self.loginwidget)
        self.loginButton.setGeometry(QtCore.QRect(20, 240, 121, 41))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setCheckable(True)
        self.loginButton.clicked.connect(self.save_login_data)

        self.lineEditUrlService = QtWidgets.QLineEdit(self.loginwidget)
        self.lineEditUrlService.setGeometry(QtCore.QRect(20, 90, 531, 31))
        self.lineEditUrlService.setObjectName("textEditUrlService")
        
        self.lineEditPassword = QtWidgets.QLineEdit(self.loginwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(20, 180, 531, 31))
        self.lineEditPassword.setObjectName("textEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.labelLoginStatus = QtWidgets.QLabel(self.loginwidget)
        self.labelLoginStatus.setGeometry(QtCore.QRect(20, 300, 281, 31))
        self.labelLoginStatus.setObjectName("labelLoginStatus")

        self.setCentralWidget(self.loginwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 27))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.labelUrlService.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">URL сервис</span></p></body></html>"))
        self.labelPassword.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Пароль</span></p></body></html>"))
        self.loginButton.setText(_translate("LoginWindow", "Войти"))
        self.labelLoginStatus.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Статус: не было входа</span></p></body></html>"))

    def save_login_data(self):
        url_saved = self.lineEditUrlService.displayText()
        password_saved = self.lineEditPassword.displayText()
        
        password_bytes = password_saved.encode('utf-8')
        password_hashed = hashlib.sha256(password_bytes).hexdigest()
        password_saved = None
        keyring.set_password(FOLDER_FOR_LOGINS, url_saved, password_hashed)
        sf.save_json_file({"URL service": url_saved}, "data/url_service.json")
        self.labelLoginStatus.setText("<html><head/><body><p><span style=\" font-size:10pt;color:#00aa00;\">Статус: данные сохранились</span></p></body></html>")

