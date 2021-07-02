from gtts import gTTS
from playsound import playsound


def save_voice(text):
    print(text)
    ttp=gTTS(text)
    ttp.save('speak_a.mp3')
    speak('speak_a.mp3')

def speak(audio_path):
    playsound(audio_path)

save_voice("Aji satya  mera")

