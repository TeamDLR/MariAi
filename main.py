from external.ActionRecognition import action_recognition

# from external.TTSRecognition import text_to_speech
# and so on...
import tkinter


def do_nothing():
    print("This button does nothing.")
    
window = tkinter.Tk()
window.title("Axela - your personal assistant")

frame = tkinter.Frame(window)
frame.pack()

# Saving Info
info_frame = tkinter.LabelFrame(frame, text="Info")
info_frame.grid(row=0, column=0, padx=20, pady=20)
for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=20)


button = tkinter.Button(frame, text="Action Recog", command=action_recognition)
button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Text To Speech", command=do_nothing)
button.grid(row=0, column=2, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Speech To Text", command=do_nothing)
button.grid(row=0, column=4, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Show Graphs", command=do_nothing)
button.grid(row=0, column=6, sticky="news", padx=20, pady=10)

button = tkinter.Button(frame, text="Questo bottone non fa niente", command=do_nothing)
button.grid(row=0, column=8, sticky="news", padx=20, pady=10)

window.mainloop()
