import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import Alarm
import Weather
import Converter
import Functions
import smtplib

print("Initializing Grace")
MASTER = "Altman"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("good morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("i am your assistant. How may I help you?")
wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumaraman.rose@gmail.ocm', 'password')
    server.sendmail("harry@gmail.com", to, content)
    server.close()


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query


# main program starting
def main():
    speak("Initializing Grace...")
    print('''
    commands:
    1)Wikipedia
    2)Open youtube
    3)Play music
    4)Time
    5)Alarm
    6)Function
    7)Converter
    7)Weather
    8)Joke
    9)Advice
    10)News
    11)Trending movies
    
          ''')
    query = takeCommand()
    main()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open('youtube.com')
        url = "youtube.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        # webbrowser.open('youtube.com')
        url = "google.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Dell\\Desktop\\Photos\\audio"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'Alarm' in query.lower():
        run_Alarm()

    elif 'Converter' in query.lower():
        import Converter

    elif 'Function' in query.lower():
        import Converter

    elif 'Weather' in query.lower():
        import Weather

    elif 'joke' in query.lower():
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

    elif "advice" in query.lower():
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

    elif "trending movies" in query.lower():
        speak(f"Some of the trending movies are: {get_trending_movies()}")
        speak("For your convenience, I am printing it on the screen sir.")
        print(*get_trending_movies(), sep='\n')

    elif 'news' in query.lower():
        speak(f"I'm reading out the latest news headlines, sir")
        speak(get_latest_news())
        speak("For your convenience, I am printing it on the screen sir.")
        print(*get_latest_news(), sep='\n')

main()