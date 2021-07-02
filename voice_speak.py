from gtts import gTTS
from playsound import playsound


def save_audio(text):
    print(text)
    ttp=gTTS(text)
    ttp.save('a.mp3')
    speak_to_text('a.mp3')

def speak_to_text(audio_path):
    playsound(audio_path)

save_audio("Hello how r u? I am fine thank you")