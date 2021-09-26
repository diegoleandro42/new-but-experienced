import datetime
import os
import webbrowser as wb

import psutil
import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia 

from jvasettings import rate, voice, volume

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    Year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today is the " + str(day) + "th"  )
    speak("of the " + str(month) +"th")
    speak("of year " + str(Year))
 
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is " + Time)


def greet():
    speak("Welcome sir ")
    speak("How can i help you ")
       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, "en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Repeat that again, plis... ")
        return "None"

    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:OneDrive\Pictures\Screenshots\ss.jpg " )

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at " + usage + "percentage")



if __name__ == "__main__":

    greet()

    while True:
        query = takeCommand()
        print(query)

        if "date" in query:
            date()  

        elif "time" in query:
            time()

        elif "offline" in query: 
            quit()

        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences= 2)
            speak(result)

        elif "open chrome" in query:
            chromepath = "C:\Program Files\Google\Chrome\Application %s"
            wb.get(chromepath).open_new_tab()

        elif "shutdown" in query:
            os.system("shutdown \s \t 1")

        elif "restart" in query:
            os.system("shutdown \r \t 1")

        elif "logout" in query:
            os.system("shutdown - 1")
            
        elif "Remember this plis" in query: 
            speak("What do you want me to remember ")
            data = takeCommand()
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close

        elif "tell me to remenber" in query:
            remember = open("data.txt", "r")
            speak("you told me to remember " + remember.read)

        elif "screenshots" in query:
            screenshot()
            speak("Done!, screenshot taken")

        elif "CPU percentage" in query: 
            cpu()