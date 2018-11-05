# -*- coding: utf8 -*-

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from importlib import reload
from fileprocess import FileProcess

reload(sys)


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.src_path[-4:] == '.hly':
            print("ECG file created:{0}".format(event.src_path))
            file_processor = FileProcess(event.src_path)
            file_processor.process_file('hly')
        elif event.src_path[-4:] == '.hlw':
            print("ECG file created:{0}".format(event.src_path))
            file_processor = FileProcess(event.src_path)
            file_processor.process_file('hlw')
        else:
            print("other file created:{0}".format(event.src_path))


def monitor(path):
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
