import requests

class CaptchaSolver:
    def __init__(self, api_key):
        self.api_key = api_key

    def solve_captcha(self, image_url):
        try:
            response = requests.post(
                "https://api.captchas.io/solve",
                json={"url": image_url},
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response_data = response.json()

            if response_data.get("status") == "success":
                captcha_text = response_data.get("text")
                return captcha_text
            else:
                error_message = response_data.get("message", "Captcha solving failed")
                print(f"Captcha Solving Error: {error_message}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return None
        except ValueError as e:
            print(f"JSON Decode Error: {e}")
            return None

# Usage
api_key = "your_api_key_here"
solver = CaptchaSolver(api_key)
captcha_text = solver.solve_captcha("captcha_image_url_here")

if captcha_text:
    print("Captcha solved:", captcha_text)
else:
    print("Captcha solving failed")