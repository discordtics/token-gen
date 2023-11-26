import threading
from modules.http_session import HttpSession
from modules.captcha import CaptchaSolver
from modules.discord_api import DiscordApi
from modules.discord_ws import DiscordWs
import json
import random
import time

class Discord:
    def __init__(self):
        self.config = json.load(open("/config.json"))
        # Other initialization code

    def start(self):
        threading.Thread(target=self.__start__).start()

    def __start__(self):
        threading.Thread(target=Console.title_thread).start()
        while True:
            if threading.active_count() < int(self.config['threads']):
                threading.Thread(target=self.generate_account).start()
                time.sleep(0.1)
