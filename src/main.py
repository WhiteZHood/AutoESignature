import threading
import os
import time
import PyQt6 as qt

import apprun as app
import websocketclient as wsclient
import codelogging as log


logger = log.logging.getLogger(__name__)

#create stop event for client
stop_event = threading.Event()

# Create and start the threads
thread_app = threading.Thread(target=app.app_run, args=(stop_event,))
current_client = wsclient.WebsocketClient()
thread_client = threading.Thread(target=current_client.start_client, args=(stop_event,))

thread_app.start()
thread_client.start()

#check here if login and password have been changed if yes, then restart client thread
last_modified_time = os.path.getmtime(current_client.file_with_url)

while not stop_event.is_set():
    time.sleep(1)
    if os.path.getmtime(current_client.file_with_url) != last_modified_time:
        print("File changed! Restarting client thread...")
        last_modified_time = os.path.getmtime(current_client.file_with_url)
        stop_event.set()
        thread_client.join()
        stop_event.clear()
        thread_client = threading.Thread(target=current_client.start_client, args=(stop_event,))
        thread_client.start()

#here we wait for threads to stop
thread_client.join()
thread_app.join()
