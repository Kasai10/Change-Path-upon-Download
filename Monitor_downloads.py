import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")
        # Run your Python script here
        subprocess.run(["python", "Interface.py"])

def start_watchdog(path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

user_home = os.path.expanduser("~")
download_folder = os.path.join(user_home, "Downloads")
start_watchdog(download_folder)
