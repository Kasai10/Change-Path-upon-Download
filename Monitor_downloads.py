import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "Interface.py")])

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

if __name__ == "__main__":
    user_home = os.path.expanduser("~")
    download_folder = os.path.join(user_home, "Downloads")
    start_watchdog(download_folder)
