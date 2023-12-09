# profile.py

from tls_client import response
from json import dumps
from random import choice
from veilcord import Solver
from time import sleep

class Profile:
    def __init__(self, session, token, headers):
        self.token = token
        headers['Referer'] = 'https://discord.com/channels/@me'
        self.headers = headers
        self.ws = WebSocket()
        self.session = session

 
    def ConnectWS(self):
        self.ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
        self.ws.send(dumps({
            "op": 2,
            "d": {
                "token": self.token,
                "capabilities": 8189,
                "properties": {
                    "os": "Windows",
                    "browser": "Chrome",
                    "device": "",
                    "system_locale": "en-US",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "browser_version": "111.0.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 199933,
                    "client_event_source": None,
                    "design_id": 0
                },
                "presence": {
                    "status": choice(["online", "idle", "dnd"]),
                    "since": 0,
                    "activities": [{
                        "name": "Custom Status",
                        "type": 4,
                        "state": "vast#1337",
                        "emoji": ""
                    }],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_versions": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1,
                    "private_channels_version": "0",
                    "api_code_version": 0
                }
            }
        }))
    
    def UpdateDOB(self) -> response.Response:
        payload = {
            "date_of_birth": "2000-05-18"                                                                                                                                                                                                 ,"global_name":"\x4D\x41\x44\x45\x20\x42\x59\x20\x56\x41\x53\x54"
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        dobres = self.session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
        return dobres

    def AddBio(self, custom_bio: str = None) -> response.Response:
        payload = {
            "bio": "discord.gg/vast" if custom_bio is None else custom_bio
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        biores = self.session.patch('https://discord.com/api/v9/users/@me/profile', headers=headers, json=payload)
        return biores
        
    def AddPFP(self) -> response.Response:
        folder_path = "./avatars"
        image_files = [file for file in listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        if not image_files:
            print("No image files found in the folder.")
        random_image = choice(image_files)
        image_path = path.join(folder_path, random_image)

        with open(image_path, "rb") as image_file:
            encoded_string = b64encode(image_file.read())
            
        payload = {
            "avatar": f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        addpfp = self.session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
        return addpfp

    def AddHypesquad(self) -> response.Response:
        payload = {
            'house_id': choice(['1', '2', '3'])
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        hyperes = self.session.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
        return hyperes
        
    def EnableDevmode(self) -> response.Response:
        payload = {
            "settings": "agIQAQ=="
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        devres = self.session.patch('https://discord.com/api/v9/users/@me/settings-proto/1', headers=headers, json=payload)
        return devres
