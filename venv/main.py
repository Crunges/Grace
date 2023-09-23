import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # Распознование речи
import datetime # Текущее время
import openai # AI
import wikipedia  # WIKI модуль
import webbrowser
import os # Управление системой
import json # json разметка
from Alarm import Alarm_ #Будильник
from Weather import Weather_ # Погода
from Converter import Convert_ # Конвертер
import smtplib
import requests # Запросы

KEY = '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' # Open-ai ключ
MASTER = "Altman"
openai.api_key = KEY

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

    print("i am your assistant. How may I help you?")
    speak("i am your assistant. How may I help you?")


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ru')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query


def generate_response(text):
    response = openai.Completion.create(
        prompt = text,
        engine = 'text-davinci-003',
        max_tokens = 500,
        temperature = 0.5,
        n = 1,
        stop = None,
        timeout = 15
    )
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None


def generate_Dalle(message):
    url = 'https://api.openai.com/v1/images/generations'

    headers = {
        'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json={'prompt': message}, headers=headers)

    if response.status_code ==200:
        result = response.json()
        print(result)
    else:
        print('Error', response.text)


def AI():
    speak('Добрый вечер, Altman')
    query = takeCommand()
    res = generate_response(f'Ты мой виртуальный помощник Grace. Кто ты?{query}')
    print(res)
    speak(res)


def AI_DALLE():
    speak('Добрый вечер, Altman')
    query = takeCommand()
    #text = input()
    generate_Dalle(query)

# main program starting
def main():
    speak("Initializing Grace...")
    print('''
    commands:
    1)Wikipedia
    4)Time
    5)Alarm
    7)Converter
    7)Weather
    8)Joke
    #9)Advice
    #10)News
    #11)Trending movies
    
          ''')
    query = takeCommand()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)


    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")


    elif 'alarm' in query.lower():
        Alarm_.run_Alarm()

    elif 'Converter' in query.lower():
        Converter.Convert_()


    elif 'Weather' in query.lower():
        Weather.Weather_()


    elif 'AI Dalle' in query.lower():
        AI_DALLE()


    elif 'AI' in query.lower():
        AI_()


    elif 'joke' in query.lower():
            speak(f"Hope you like this one sir")
            headers = {
            'Accept': 'application/json'
            }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            return res["joke"]

    # elif "advice" in query.lower():
    #         speak(f"Here's an advice for you, sir")
    #         advice = get_random_advice()
    #         speak(advice)
    #         speak("For your convenience, I am printing it on the screen sir.")
    #         print(advice)
    #
    # elif "trending movies" in query.lower():
    #     speak(f"Some of the trending movies are: {get_trending_movies()}")
    #     speak("For your convenience, I am printing it on the screen sir.")
    #     print(*get_trending_movies(), sep='\n')
    #
    # elif 'news' in query.lower():
    #     speak(f"I'm reading out the latest news headlines, sir")
    #     speak(get_latest_news())
    #     speak("For your convenience, I am printing it on the screen sir.")
    #     print(*get_latest_news(), sep='\n')

wishMe()
main()