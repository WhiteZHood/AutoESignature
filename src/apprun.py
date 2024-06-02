import qdarktheme
import ctypes
import time

import storingfiles as sf
import codelogging as log
import websocketclient as wsclient
from tray import *


def app_run(stop_event):
    import sys # Only needed for access to command line arguments
    
    logger = log.logging.getLogger(__name__)
    
    try:
        # You need one (and only one) QApplication instance per application.
        # Pass in sys.argv to allow command line arguments for your app.
        # If you know you won't use command line arguments QApplication([]) works too.
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QIcon("AutoESignature_logo.png"))
        app.setQuitOnLastWindowClosed(False) #uncomment if we want that app will not close after closure of window
        
        if (sf.load_json_file("data/settings_setted.json")["darkModeOn"] == "True"):
            qdarktheme.setup_theme("dark")
        else:
            qdarktheme.setup_theme("light")
        
        myappid = 'AutoESign.AutoESign.AutoESign.0.0' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        tray_icon = SystemTrayIcon(QIcon("AutoESignature_logo.png"), app)
        tray_icon.setVisible(True)
        tray_icon.show()
        
        app.exec() 
        stop_event.set() 

    except (SystemExit):
        # Обработка завершения работы приложения
        stop_event.set()

    # Your application won't reach here until you exit and the event
    # loop has stopped.

# to create exe of the program: pyinstaller --onefile main.py
