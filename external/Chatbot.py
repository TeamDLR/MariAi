import requests


class Chatbot:
    openai_api_key = None
    url = "https://api.openai.com/v1/chat/completions"
    headers = {}
    base_context = ""

    def __init__(self, openai_api_key=None, base_context=None):
        self.openai_api_key = openai_api_key

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api_key}",
        }

        if base_context:
            self.base_context = base_context
        else:
            self.base_context = "You are Axela, an assistant that respond brieflY based on the action and prompt written on the prompt."

    def send_chatgpt_request(self, action, prompt):
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": self.base_context,
                },
                {
                    "role": "user",
                    "content": f'Action: "{action}" Prompt: "{prompt}", what will you say to help me?',
                },
            ],
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print(response.json()["choices"][0]["message"]["content"])
            return response.json()["choices"][0]["message"]["content"]
        else:
            print("Error:", response.status_code, response.text)
