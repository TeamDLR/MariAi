#pip install SpeechRecognition pyaudio pynput
import speech_recognition as sr
import pyaudio
from pynput import keyboard
import threading
def run_speech_to_text():
    p = pyaudio.PyAudio()

    print("Dispositivi audio disponibili:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']} - Input Channels: {info['maxInputChannels']}")

    device_index = 3 

    info = p.get_device_info_by_index(device_index)
    if info['maxInputChannels'] == 0:
        raise ValueError(f"Il dispositivo selezionato (indice {device_index}) non è un microfono o non ha canali di input.")

    r = sr.Recognizer()

    stop_listening = False

    def on_press(key):
        global stop_listening
        if key == keyboard.Key.space:
            stop_listening = True
            return False  

    def listen_audio():
        global stop_listening
        with sr.Microphone(device_index=device_index) as source:
            print(f"Usando il microfono: {info['name']}")
            print("Parla ora (premi barra spaziatrice per terminare):")
            stop_listening = False
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            while not stop_listening:
                try:
                    audio = r.listen(source, timeout=5)  
                    break
                except sr.WaitTimeoutError:
                    if stop_listening:
                        break
                    continue
            listener.stop()
        return audio

    audio = listen_audio()

    try:
        text = r.recognize_google(audio, language="en-US ")
        print("Testo riconosciuto: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition non ha capito l'audio")
    except sr.RequestError as e:
        print("Errore nel servizio Google Speech Recognition; {0}".format(e))

    p.terminate()