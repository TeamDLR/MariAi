# from external.TTSRecognition import text_to_speech
# and so on...
import os
import tkinter

from external.ActionRecognition import run_action_recognition
from external.Chatbot import Chatbot
from external.SpeechToText import run_speech_to_text
from external.TextToSpeech import run_text_to_speech

# Load environment variables from .env file
try:
    with open("secrets.env") as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value
except FileNotFoundError:
    print(
        "\n[WARNING] No secrets.env file found. Please create one with the required keys. External APIs will not work.\n"
    )


def do_nothing():
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def real_action_recognition():
    USE_WEBCAM = False
    cam_id = 0
    # video_file_2 = "https://archive.org/serve/ISSVideoResourceLifeOnStation720p/ISS%20Video%20Resource_LifeOnStation_720p.mp4"
    # video_file_3 = "https://ia801304.us.archive.org/13/items/bctvnj-Cooking_Eggs_for_Family/Cooking_Eggs_for_Family.mpeg4"
    # video_file_4 = "https://dn720404.ca.archive.org/0/items/80-year-old-man-chopping-wood/80%20Year%20Old%20Man%20Chopping%20Wood.mp4"
    video_file = "https://ia600609.us.archive.org/26/items/Game_of_the_Week_Play_of_the_Game_-_Charles_Alexander_Block_Basket_and_1/Game_of_the_Week_Play_of_the_Game_-_Charles_Alexander_Block_Basket_and_1.mp4"
    source = cam_id if USE_WEBCAM else video_file
    additional_options = (
        {"skip_first_frames": 600, "flip": False} if not USE_WEBCAM else {"flip": True}
    )
    return run_action_recognition(
        source=source, use_popup=True, threshold=0.5, **additional_options
    )


def real_text_to_speech():
    filepath = "./output.mp3"
    user_input = input("Inserisci qualcosa: ")

    run_text_to_speech(user_input, filepath)


def real_speech_to_text(language_code="en-US"):
    return run_speech_to_text(language_code)


def real_chatbot():
    Chatbot(openai_api_key=os.environ["OPENAI_API_KEY"]).send_chatgpt_request(
        "Cooking", "Can you find some recipies?"
    )


def demo_all_in_one():
    # Step 0: STT
    text = real_speech_to_text(language_code="it-IT").lower()

    if "maria" in text:
        text = text.split("maria")[1]

    print(f"What you said: {text}")

    # Step 1: Show the video and recognize action
    action = real_action_recognition()
    print(f"Action recognized: {action}")

    # Step 2: Use the action to form a question
    question = f"{text}"

    # Step 3: Get response from OpenAI
    chatbot = Chatbot(openai_api_key=os.environ["OPENAI_API_KEY"])
    response = chatbot.send_chatgpt_request(action, question)

    print(f"CHATGPT: {response}")

    # Step 4: Convert the response to speech
    filepath = "output.mp3"
    run_text_to_speech(response, filepath)


window = tkinter.Tk()
window.title("Axela - your personal assistant")

frame = tkinter.Frame(window)
frame.pack()

# Saving Info
info_frame = tkinter.LabelFrame(frame, text="Info")
info_frame.grid(row=0, column=0, padx=20, pady=20)
for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=20)


button = tkinter.Button(frame, text="Action Recog", command=real_action_recognition)
button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Text To Speech", command=real_text_to_speech)
button.grid(row=0, column=2, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Speech To Text", command=real_speech_to_text)
button.grid(row=0, column=4, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Show Graphs", command=do_nothing)
button.grid(row=0, column=6, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Chatbot", command=real_chatbot)
button.grid(row=0, column=8, sticky="news", padx=20, pady=12)

button = tkinter.Button(frame, text="Demo All-in-One", command=demo_all_in_one)
button.grid(row=0, column=10, sticky="news", padx=20, pady=12)

window.mainloop()
