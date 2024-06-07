from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def play_audio(source):
    """
    Play Audio using pydub library
    """
    audio = AudioSegment.from_mp3(source)
    speed_factor = 1.2
    sped_up_audio = audio.speedup(playback_speed=speed_factor)
    play(sped_up_audio)


def generate_audio(user_input, filepath):
    """
    Generate using GoogleTTS a short
    audio clip
    """
    gTTS(text=user_input, lang="it").save(filepath)


def run_text_to_speech(user_input, filepath):
    generate_audio(user_input, filepath)
    play_audio(filepath)
