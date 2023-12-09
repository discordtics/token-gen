
class Discord:
    def __init__(self) -> None:
        self.proxy = (choice(open("./proxies.txt", "r").readlines()).strip()
            if len(open("./proxies.txt", "r").readlines()) != 0
            else None)
        self.session = Session(
            client_identifier="chrome_113",
            random_tls_extension_order=True
        )
        self.session.proxies = {
            "http": "http://" + self.proxy,
            "https": "http://" + self.proxy
        }
                
                
    def getCookies(self) -> list:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Track': xtrack,
        }

        response = self.session.get('https://discord.com/api/v9/experiments', headers=headers)
        return response.cookies, response.json().get("fingerprint")
    

    def register(self) -> bool:
        try:
            xcookies, fingerprint = self.getCookies()
            cookies = {
                '__dcfduid': xcookies.get('__dcfduid'),
                '__sdcfduid': xcookies.get('__sdcfduid'),
                '__cfruid': xcookies.get('__cfruid'),
                'locale': 'en-US',
            }
            config = load('config.toml')
            captchaService = config.get("captcha").get("service")
            key = config.get("captcha").get("capKey")
            capKey = Solver(self.session, captchaService, key, "4c672d35-0701-42b2-88c3-78380b0db560").solveCaptcha()

            payload = {
                "consent": True,
                "fingerprint": fingerprint,
                "username": "vastdabest" if CONFIG_uname == "" else CONFIG_uname,
                "captcha_key": capKey,
                "invite": "vast"
            }
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'content-length': str(len(dumps(payload))),
                'Content-Type': 'application/json',
                'Origin': 'https://discord.com',
                'Referer': 'https://discord.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 12.5; XBOX Build/NHG47K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36',
                'X-Fingerprint': fingerprint,
                'X-Track': xtrack,
            }

            response = self.session.post('https://discord.com/api/v9/auth/register', headers=headers, cookies=cookies, json=payload)
            if "token" not in response.text:
                if "retry_after" in response.text:
                    Console.printf(f"(-) RateLimit: {response.json().get('retry_after')}")
                    return False
                Console.printf(f"(-) Failed to gen: {response.text}")
                return False

            token = response.json().get('token')

            headers.pop('content-length')
            headers.pop('X-Fingerprint')
            headers['Authorization'] = token
            status = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers)
            if status.status_code != 200:
                if CONFIG_showLock:
                    Console.printf(f"(-) Locked Token: {token} [{status.status_code}]")
                Stats.locked += 1
                with open("./locked.txt", "a+") as f:
                    f.write(f"{token}\n")
                return False

            Console.printf(f"(+) {token}")
            Stats.unlocked += 1
            with open("./unlocked.txt", "a+") as f:
                f.write(f"{token}\n")
            
            profile = Profile(self.session, token, headers)
            profile.ConnectWS()
            profile.UpdateDOB()

            humanizer = "(*) HUMANIZED | ("

            if CONFIG_addBio:
                biores = profile.AddBio()
                if biores.status_code == 200:
                    humanizer += "BIO"

            if CONFIG_addHype:
                hyperes = profile.AddHypesquad()
                if hyperes.status_code == 204:
                    if CONFIG_addBio:
                        humanizer += ", "
                    humanizer += "HYPE"

            if CONFIG_enableDev:
                devres = profile.EnableDevmode()
                if devres.status_code == 200:
                    if CONFIG_addBio or CONFIG_addHype:
                        humanizer += ", "
                    humanizer += "DEVMODE"

            if CONFIG_addPFP:
                pfpres = profile.AddPFP()
                if pfpres.status_code == 200:
                    if CONFIG_addBio or CONFIG_addHype or CONFIG_enableDev:
                        humanizer += ", "
                    humanizer += "PFP"

            Console.printf(f"{humanizer})")

                
            return True
        except Exception as e:
            Console.printf(f"(!) ExC: {e}")