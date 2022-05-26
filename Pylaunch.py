import re
import pyttsx3
import speech_recognition as rs 
import pywhatkit

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
                rec = rec.replace(nombre, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = lisen()
    
    if 'Listen' in rec:
        song = rec.replace('Listen', '')
        talk('reproduciendo' + song)
        pywhatkit.playonyt(song)

    elif 'send' in rec:
        envio = rec.replace('send', '')
        talk('enviando mensaje')
        pywhatkit.sendwhatmsg("phone number",envio,21,28,10)

    elif 'search' in rec:
        search = rec.replace('search','')
        talk('Buscando' + search)
        pywhatkit.search(search)
run()