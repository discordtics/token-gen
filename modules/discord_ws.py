import websocket
import json
import threading

class DiscordWs:
    def __init__(self, token):
        self.token = token
        self.ws = None
        self.running = False

    def connect(self):
        url = f"wss://gateway.discord.gg/?v=9&encoding=json"
        headers = {
            "Authorization": f"Bot {self.token}"
        }
        
        try:
            self.ws = websocket.WebSocketApp(url, header=headers, on_message=self.on_message)
            self.ws.run_forever()
        except websocket.WebSocketException as e:
            print(f"WebSocket Error: {e}")

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            event_type = data.get('t', '')

            if event_type == 'READY':
                self.handle_ready(data)
            elif event_type == 'MESSAGE_CREATE':
                self.handle_message(data)
            # Add more event handlers as needed
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")

    def handle_ready(self, data):
        print("Bot is ready:", data['d']['user']['username'])

    def handle_message(self, data):
        content = data['d']['content']
        author = data['d']['author']['username']
        print(f"Received message from {author}: {content}")

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.connect).start()

    def stop(self):
        self.running = False
        if self.ws:
            self.ws.close()