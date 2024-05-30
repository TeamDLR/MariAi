# from external.TTSRecognition import text_to_speech
# and so on...
import tkinter

from external.ActionRecognition import run_action_recognition
from external.SpeechToText import run_speech_to_text
from external.TextToSpeech import run_text_to_speech


def do_nothing():
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def real_action_recognition():
    USE_WEBCAM = False
    cam_id = 0
    video_file = "https://archive.org/serve/ISSVideoResourceLifeOnStation720p/ISS%20Video%20Resource_LifeOnStation_720p.mp4"
    source = cam_id if USE_WEBCAM else video_file
    additional_options = (
        {"skip_first_frames": 600, "flip": False} if not USE_WEBCAM else {"flip": True}
    )
    run_action_recognition(source=source, use_popup=True, **additional_options)


def real_text_to_speech():
    filepath = "./output.mp3"
    user_input = input("Inserisci qualcosa: ")

    run_text_to_speech(user_input, filepath)


def real_speech_to_text():
    run_speech_to_text()


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

button = tkinter.Button(frame, text="Questo bottone non fa niente", command=do_nothing)
button.grid(row=0, column=8, sticky="news", padx=20, pady=10)

window.mainloop()
