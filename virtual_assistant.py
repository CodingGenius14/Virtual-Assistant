import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(user_audio):
    # Get audio
    engine.say(user_audio)
    engine.runAndWait()


def greeting():
    time = datetime.datetime.now().hour
    if 0 <= time <= 12:
        speak("Good Morning, Vikram")
    else:
        speak("Good Evening, Vikram")


def take_in_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Sorry could not understand")
        return 'none'
    return query


if __name__ == '__main__':
    while True:
        query = take_in_audio().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)

        # Open Web Browsers
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
        elif 'open google classroom' in query:
            speak('Opening Google Classroom')
            webbrowser.open('classroom.google.com')
        elif 'open gmail' in query:
            speak('Opening your gmail')
            webbrowser.open('gmail.com')
        elif 'open spotify' in query:
            speak('Opening spotify')
            webbrowser.open('spotify.com')
        elif 'open coin market cap' in query:
            speak('Opening coin market cap')
            webbrowser.open('coinmarketcap.com')
        elif 'open linkedin' in query:
            speak('Opening Linkedin')
            webbrowser.open('linkedin.com')
        elif 'open discord' in query:
            speak('Opening discord')
            webbrowser.open('discord.com')
        elif 'open delta math' in query:
            speak('Opening delta math')
            webbrowser.open('deltamath.com')
        elif 'open codio' in query:
            speak('Opening codio')
            webbrowser.open('codio.com')
        elif 'open chess.com' in query:
            speak('Opening Chess.com')
            webbrowser.open('chess.com')
        elif 'github' in query:
            speak("Opening Github")
            webbrowser.open('github.com')

        # Open Code Editors
        elif 'open vs code' in query:
            vs_code_path = 'C:\\Users\\kanik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(vs_code_path)
        elif 'open pie charm' in query:
            pycharm_code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_code_path)
