from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import qdarktheme
import os
import pathlib
from win32com.client import Dispatch

import hashes.signinghashes as sh
import storingfiles as sf

def create_boost_shortcut():
    path = f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"  #This is where the shortcut will be created
    target = f"dist/program.exe" # directory to which the shortcut is created

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.save()

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("SettingsWindow")
        self.resize(768, 430)

        self.settingswidget = QtWidgets.QWidget(self)
        self.settingswidget.setObjectName("settingswidget")

        saved_dict_settings = sf.load_json_file("data/settings_setted.json")

        self.checkBoxOnWithSystemBoot = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxOnWithSystemBoot.setGeometry(QtCore.QRect(10, 51, 342, 21))
        self.checkBoxOnWithSystemBoot.setObjectName("checkBoxOnWithSystemBoot")
        if saved_dict_settings["withSystemBootOn"] == "True":
            self.checkBoxOnWithSystemBoot.setChecked(True)
        
        self.checkBoxDarkModeOn = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxDarkModeOn.setGeometry(QtCore.QRect(10, 107, 108, 21))
        self.checkBoxDarkModeOn.setObjectName("checkBoxDarkModeOn")
        if saved_dict_settings["darkModeOn"] == "True":
            self.checkBoxDarkModeOn.setChecked(True)
        
        self.SettingsLabel = QtWidgets.QLabel(self.settingswidget)
        self.SettingsLabel.setGeometry(QtCore.QRect(10, 10, 156, 34))
        self.SettingsLabel.setObjectName("SettingsLabel")

        self.saveButton = QtWidgets.QPushButton(self.settingswidget)
        self.saveButton.setGeometry(QtCore.QRect(10, 216, 97, 29))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setCheckable(True)
        self.saveButton.clicked.connect(self.save_settings)

        self.SerialNumberLabel = QtWidgets.QLabel(self.settingswidget)
        self.SerialNumberLabel.setGeometry(QtCore.QRect(10, 160, 221, 23))
        self.SerialNumberLabel.setObjectName("SerialNumberLabel")

        self.SerialNumberEdit = QtWidgets.QLineEdit(self.settingswidget)
        self.SerialNumberEdit.setGeometry(QtCore.QRect(290, 160, 410, 23))
        self.SerialNumberEdit.setObjectName("SerialNumberEdit")
        self.SerialNumberEdit.setText(sf.load_json_file("data/settings_setted.json")["Certificate Serial Number"])
        
        self.checkBoxConnectionIcon = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxConnectionIcon.setGeometry(QtCore.QRect(10, 79, 335, 21))
        self.checkBoxConnectionIcon.setObjectName("checkBoxConnectionIcon")
        if saved_dict_settings["connectionIconOn"] == "True":
            self.checkBoxConnectionIcon.setChecked(True)

        self.savingStatus = QtWidgets.QLabel(self.settingswidget)
        self.savingStatus.setGeometry(QtCore.QRect(120, 220, 221, 21))
        self.savingStatus.setObjectName("savingStatus")

        self.setCentralWidget(self.settingswidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 27))
        self.menubar.setObjectName("menubar")

        self.settingsMenu = QtWidgets.QMenu(self.menubar)
        self.settingsMenu.setObjectName("settingsMenu")

        self.designMenu = QtWidgets.QMenu(self.menubar)
        self.designMenu.setObjectName("designMenu")

        self.aboutMenu = QtWidgets.QMenu(self.menubar)
        self.aboutMenu.setObjectName("aboutMenu")

        self.setMenuBar(self.menubar)

        self.menubar.addAction(self.settingsMenu.menuAction())
        self.menubar.addAction(self.designMenu.menuAction())
        self.menubar.addAction(self.aboutMenu.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.checkBoxOnWithSystemBoot.setText(_translate("SettingsWindow", "Открывать приложение с запуском компьютера"))
        self.checkBoxDarkModeOn.setText(_translate("SettingsWindow", "Темная тема"))
        self.SettingsLabel.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Настройки</span></p></body></html>"))
        self.saveButton.setText(_translate("SettingsWindow", "Сохранить"))
        self.SerialNumberLabel.setText(_translate("SettingsWindow", "<html><head/><body><p>Серийный номер сертификата ЭП</p></body></html>"))
        self.checkBoxConnectionIcon.setText(_translate("SettingsWindow", "Показывать на иконке состояние подключения"))
        self.settingsMenu.setTitle(_translate("SettingsWindow", "Настройки"))
        self.designMenu.setTitle(_translate("SettingsWindow", "Тема"))
        self.aboutMenu.setTitle(_translate("SettingsWindow", "О программе"))
        self.savingStatus.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" color:#7c7c7c;\">Статус: нет изменений</span></p></body></html>"))
    
    def save_settings(self):
        dict_settings = sf.load_json_file("data/settings_setted.json")

        if (self.checkBoxOnWithSystemBoot.isChecked()):
            dict_settings["withSystemBootOn"] = "True"
            #create_boost_shortcut()
        else:
            dict_settings["withSystemBootOn"] = "False"
            #pathlib.Path.unlink(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/program.exe")

        if (self.checkBoxDarkModeOn.isChecked()):
            qdarktheme.setup_theme("dark")
            dict_settings["darkModeOn"] = "True"
        else:
            qdarktheme.setup_theme("light")
            dict_settings["darkModeOn"] = "False"

        if (self.checkBoxConnectionIcon.isChecked()):
            dict_settings["connectionIconOn"] = "True"
        else:
            dict_settings["connectionIconOn"] = "False"

        certificateSerialNumber = sh.format_serial_number(self.SerialNumberEdit.displayText())
        dict_settings["Certificate Serial Number"] = certificateSerialNumber

        sf.save_json_file(dict_settings, "data/settings_setted.json")
        self.savingStatus.setText("<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Статус: изменения сохранены</span></p></body></html>")
