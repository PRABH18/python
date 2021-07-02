import speech_recognition as sr
voice=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    audio=voice.listen(source)
    try:
        text=voice.recognize_google(audio)
        print("you said",text)
    except:
        print("your voice is Not clear")