import random
from plyer import notification
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[1])
newVoiceRate = 145
engine.setProperty('rate' , newVoiceRate)

# print(voice[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Read_quotes():
    with open("quotes.txt", encoding="utf8") as f:
        text = f.readlines()
        # print(text)
        random_quotes = random.choice(text)
        return random_quotes


def get_notification(quotes):
    notification.notify(
        title="Today Motivation Quotes",
        message=quotes,
        app_icon='F:\My Project\Motivationl Quotes Notification\img.ico',
        timeout=5
    )


if __name__ == "__main__":
    while(True):
        quotes = Read_quotes()
        get_notification(quotes)
        speak(quotes)
        time.sleep(10)

