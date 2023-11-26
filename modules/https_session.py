import httpx

class HttpSession:
    def __init__(self, proxy):
        self.proxy = proxy
        self.http_client = httpx.Client(proxies={'http': self.proxy})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.http_client:
            self.http_client.close()

    def get(self, url, params=None, headers=None):
        try:
            response = self.http_client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e:
            print(f"HTTP GET Error: {e}")
            return None

    def post(self, url, data=None, headers=None):
        try:
            response = self.http_client.post(url, data=data, headers=headers)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e:
            print(f"HTTP POST Error: {e}")
            return None

    def get_cookies(self):
        response = self.get("https://example.com")
        if response:
            cookies = response.cookies
            return cookies
        return None