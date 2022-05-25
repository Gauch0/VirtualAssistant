import pyttsx3
import speech_recognition as rs 

nombre = 'Matthias'

listener = rs.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(texto):
    engine.say(texto)
    engine.runAndWait()

def lisen():
    try:
        with rs.Microphone() as source:
            print("Esto se esta escuchando..!")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            if nombre in rec:
                print(talk(rec))
    except:
        pass
    return rec

def run():
    rec = lisen()
    if 'reproduce' in rec:
        print('Reproduciendo')
run()