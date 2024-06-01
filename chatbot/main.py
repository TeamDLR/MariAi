import requests

openai_api_key = "insert-your-openai-key"

if openai_api_key is None:
    raise ValueError("OpenAI API key is not set in environment variables.")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are Axela, a home assistant that respond briefly based on the action and prompt written on the prompt. You will ignore the Action if it has nothing to do with the prompt",
        },
        {
            "role": "user",
            "content": 'Action: " Cooking chicken " Prompt: " Can you find some recipies? ", what will you say to help me?',
        },
    ],
}


def send_chatgpt_request():
    response = requests.post(url, headers=headers, json=data)
    print("hello")
    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print("\n")
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print("Error:", response.status_code, response.text)


send_chatgpt_request()
