import requests
import os
from dotenv import load_dotenv
load_dotenv()
class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.api_key = os.getenv("API_KEY")

    def _send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.request(method, url, headers=headers, json=data)

        print(response)

        return response.status_code, response.json()
