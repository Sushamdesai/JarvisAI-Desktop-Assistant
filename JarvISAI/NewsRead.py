import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9cda07e4e6fe4b99a45f259481953fbe",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9cda07e4e6fe4b99a45f259481953fbe",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9cda07e4e6fe4b99a45f259481953fbe",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9cda07e4e6fe4b99a45f259481953fbe",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9cda07e4e6fe4b99a45f259481953fbe",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9cda07e4e6fe4b99a45f259481953fbe"
    }

    url = None
    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
    if url is None:
        print("URL not found")
        return

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    articles = news["articles"]
    for article in articles:
        title = article["title"]
        print(title)
        speak(title)
        news_url = article["url"]
        print(f"For more info visit: {news_url}")

        choice = input("[Press 1 to continue] and [Press 2 to stop]")
        if choice == "2":
            break

    speak("That's all")

latestnews()
