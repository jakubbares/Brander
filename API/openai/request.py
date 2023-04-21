
import requests

class OpenAIRequest:
    def __init__(self):
        self.host = ""


    def get_response_from_prompt(self, prompt: str):
        response = requests.post()
