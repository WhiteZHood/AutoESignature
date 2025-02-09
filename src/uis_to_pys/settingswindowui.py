# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(718, 310)
        self.settingswidget = QtWidgets.QWidget(SettingsWindow)
        self.settingswidget.setObjectName("settingswidget")
        self.checkBoxOnWithSystemBoot = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxOnWithSystemBoot.setGeometry(QtCore.QRect(10, 51, 342, 21))
        self.checkBoxOnWithSystemBoot.setObjectName("checkBoxOnWithSystemBoot")
        self.checkBoxDarkModeOn = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxDarkModeOn.setGeometry(QtCore.QRect(10, 107, 108, 21))
        self.checkBoxDarkModeOn.setObjectName("checkBoxDarkModeOn")
        self.SettingsLabel = QtWidgets.QLabel(self.settingswidget)
        self.SettingsLabel.setGeometry(QtCore.QRect(10, 10, 156, 34))
        self.SettingsLabel.setObjectName("SettingsLabel")
        self.saveButton = QtWidgets.QPushButton(self.settingswidget)
        self.saveButton.setGeometry(QtCore.QRect(10, 216, 97, 29))
        self.saveButton.setAutoFillBackground(False)
        self.saveButton.setCheckable(True)
        self.saveButton.setChecked(False)
        self.saveButton.setObjectName("saveButton")
        self.SerialNumberLabel = QtWidgets.QLabel(self.settingswidget)
        self.SerialNumberLabel.setGeometry(QtCore.QRect(10, 160, 221, 23))
        self.SerialNumberLabel.setTextFormat(QtCore.Qt.AutoText)
        self.SerialNumberLabel.setObjectName("SerialNumberLabel")
        self.SerialNumberEdit = QtWidgets.QLineEdit(self.settingswidget)
        self.SerialNumberEdit.setGeometry(QtCore.QRect(290, 160, 410, 23))
        self.SerialNumberEdit.setObjectName("SerialNumberEdit")
        self.checkBoxConnectionIcon = QtWidgets.QCheckBox(self.settingswidget)
        self.checkBoxConnectionIcon.setGeometry(QtCore.QRect(10, 79, 335, 21))
        self.checkBoxConnectionIcon.setObjectName("checkBoxConnectionIcon")
        self.label = QtWidgets.QLabel(self.settingswidget)
        self.label.setGeometry(QtCore.QRect(120, 220, 221, 21))
        self.label.setObjectName("label")
        SettingsWindow.setCentralWidget(self.settingswidget)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 27))
        self.menubar.setObjectName("menubar")
        self.settingsMenu = QtWidgets.QMenu(self.menubar)
        self.settingsMenu.setObjectName("settingsMenu")
        self.designMenu = QtWidgets.QMenu(self.menubar)
        self.designMenu.setObjectName("designMenu")
        self.aboutMenu = QtWidgets.QMenu(self.menubar)
        self.aboutMenu.setObjectName("aboutMenu")
        SettingsWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.settingsMenu.menuAction())
        self.menubar.addAction(self.designMenu.menuAction())
        self.menubar.addAction(self.aboutMenu.menuAction())

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.checkBoxOnWithSystemBoot.setText(_translate("SettingsWindow", "Открывать приложение с запуском компьютера"))
        self.checkBoxDarkModeOn.setText(_translate("SettingsWindow", "Темная тема"))
        self.SettingsLabel.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Настройки</span></p></body></html>"))
        self.saveButton.setText(_translate("SettingsWindow", "Сохранить"))
        self.SerialNumberLabel.setText(_translate("SettingsWindow", "<html><head/><body><p>Серийный номер сертификата ЭП</p></body></html>"))
        self.checkBoxConnectionIcon.setText(_translate("SettingsWindow", "Показывать на иконке состояние подключения"))
        self.label.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" color:#7c7c7c;\">Статус: нет изменений</span></p></body></html>"))
        self.settingsMenu.setTitle(_translate("SettingsWindow", "Настройки"))
        self.designMenu.setTitle(_translate("SettingsWindow", "Тема"))
        self.aboutMenu.setTitle(_translate("SettingsWindow", "О программе"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
