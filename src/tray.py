from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
import subprocess as sp

from loginwindow import *
from settingswindow import *


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, app, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("AutoESignature")
        self.app = app

        menu = QMenu(parent)
        view_logs = menu.addAction("Посмотреть логи")
        documentation = menu.addAction("Документация")
        user_manual = menu.addAction("Руководство пользователя")
        settings = menu.addAction("Настройки")
        exit_ = menu.addAction("Выход")
        exit_.triggered.connect(self.exit_app)
        
        self.setContextMenu(menu)
        self.activated.connect(self.trayiconclicked)

        settings.triggered.connect(self.settings_clicked)
        user_manual.triggered.connect(self.user_manual_clicked)
        documentation.triggered.connect(self.documentation_clicked)
        view_logs.triggered.connect(self.view_logs_clicked)
    
    def exit_app(self):
        self.hide()
        self.app.quit()

    def trayiconclicked(self, reason):
        if reason == self.ActivationReason.Trigger:
            cur_win = LoginWindow()
            self.win = cur_win
            cur_win.show()
    
    def settings_clicked(self):
        cur_win = SettingsWindow()
        self.win = cur_win
        cur_win.show()
    
    def user_manual_clicked(self):
        pass

    def documentation_clicked(self):
        pass
    
    def view_logs_clicked(self):
        programName = "notepad.exe"
        fileName = "data/logging.log"
        sp.Popen([programName, fileName])
