import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyjokes # pip install pyjokes
from datetime import date
import time
import requests




sir = "Ankur"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#wish me function
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning sir.")
    
    elif hour >=12 and hour < 16:
        speak("Good noon sir.")
    
    elif hour >=16 and hour < 18:
        speak("Good afternoon sir.")

    else:
        speak("Good evening sir.")
    assistantName = ("Jarvis")
    speak(assistantName+" is at your service sir")
    # speak("I'm your assistant" +assistantName)
    # speak("How may i help you sir")

# for play music
def playMusic():
                try:
                    speak("Here you go with music")
                    music_dir = 'C:\\Users\\Ankur\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as e:
                    speak("YT music is opening sir.")
                    webbrowser.open("music.youtube.com")


#take microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 

        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        print(" Speech Recognition could not understand audio")
        return "None"
    
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

#main function
if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()
        if query == "None":
            continue
        # Logic for executing tasks based on query

        #for the results from wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        #for opening some popular websites
        elif 'open google' in query:
            speak("Google is opening sir.")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("Stackoverflow is opening sir.")
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            speak("Github is opening sir.")
            webbrowser.open("github.com")
        elif 'open youtube' in query:
            speak("Youtube is opening sir.")
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            speak("Facebook is opening sir.")
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            speak("Instagram is opening sir.")
            webbrowser.open("instagram.com")
        elif 'open codeforces' in query:
            speak("Codeforces is opening sir.")
            webbrowser.open("codeforces.com")
        elif 'open codechef' in query:
            speak("Codechef is opening sir.")
            webbrowser.open("codechef.com")
        elif 'open chat GPT' in query:
            speak("Chat GPT is opening sir.")
            webbrowser.open("chat.openai.com")
        
        #for playing musics
        elif 'play music' in query or "play song" in query:
            playMusic()

                


        #for telling the time
        elif 'time now' in query or "the time" in query or "what is the time" in query:
            timeNow = datetime.datetime.now().strftime("%H %M")
            print(timeNow)
            speak(f"Sir, the time is{timeNow}") 

        #for opening some software by command
        elif 'open chrome' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            speak("Google chrome is opening sir")
            os.startfile(chromePath)
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Ankur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("VS Code is opening sir")
            os.startfile(codePath)

        #logic for some Q&A
        elif 'how are you' in query:
            speak("I am fine. And you Sir")
        elif 'i am fine' in query or 'i am good' in query or "i am well" in query:
            speak("It's good to know that you're well")
        elif 'i am not fine' in query or 'i am not good' in query or "i am not well" in query or "not fine" in query:
            speak("it's your problem , i don't care ")
        elif "what's your name" in query or "what is your name" in query or "your name" in query:
            assistantName = ("Jarvis")
            speak("My friends call me"+ assistantName)
            print("My friends call me", assistantName)
        elif "who made you" in query or "who created you" in query:
            speak (f"I have been created by {sir}")
            print(f"I have been created by {sir}")
        elif "who am i" in query:
            speak("If you talk then definitely you're human")
            print("If you talk then definitely you're human")
        elif "why you came to the world" in query or "how you came to the world" in query:
            speak("Thanks to Ankur. further It's a secret")
            print("Thanks to Ankur. further It's a secret")
        elif "what is love" in query:
            speak("It's 7th sense that destroy all other senses")
            print("It's 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I'm your virtual assistant")
            print("I'm your virtual assistant")
        elif "good morning" in query:
            speak("A warm" +query)
            speak("How are you sir")
        elif "exit" in query:
            speak("Thanks for giving me your time")
            speak("I'm always here when you need me")
            exit()
        #most asked question from google Assistant
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("Never")
            print("You stand alon my friend!")
        elif "i love you" in query:
            speak("I don't care")
            print("don't confuse me")
        elif "will you be my friend" in query:
            speak("I am already")
            print("WHY?")
        elif "sing a song" in query:
            speak("I wish I were able to. but i can play some songs for you sir. May i?")
            print("I wish I were able to. but i can play some songs for you sir. May i?")
            query = takeCommand()
            if "yes" in query or "sure" in query:
                playMusic()
        
        # asking for a joke
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        # asking for search something over the internet
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            speak("I'm searching" +query)
            webbrowser.open(query)

        # write a note by Ruby
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            textfile = open("note.txt", 'w')
            speak("Sir, Should i include date and time")
            date_time = takeCommand()
            if 'yes' in date_time or 'sure' in date_time:
                speak("done, sir")
                date_today = date.today()
                strDate = date_today.strftime("%d/%m/%Y ")
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                textfile.write(strDate)
                textfile.write(strTime)
                textfile.write(" : \n")
                textfile.write(note)
                textfile.close()
            else:
                textfile.write(note)
                textfile.close()
        
        # show the saved note by voice command
        elif "show note" in query or "open note" in query :
            speak("Showing notes")
            textfile = open("note.txt", "r")
            print(textfile.read())
            speak(textfile.read())

        # asking ruby for any location
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("I locating"+location)
            webbrowser.open("https://www.google.com/maps/search/" + location + "")

        # asking Ruby to translate english to bengali
        elif "translate" in query:
            speak("What should i translate sir")
            query = takeCommand()
            translate = query
            speak("your translation is ready sir")
            webbrowser.open("https://translate.google.com/?sl=en&tl=bn&text="+translate+"&op=translate")

        # I forbidding ruby to listen to me
        elif "don't listen" in query or "stop listening" in query:
            speak("How much time do you want to stop me from listening to commands, sir")
            query = takeCommand() #only say the digit please
            duration = int(query)
            duration = duration * 60
            speak("Okay, sir, I'll don't listen to you for"+query+"minute")
            time.sleep(duration)
            speak("Hello sir, Now I'm listening to your commands")

        # asking ruby for google direction from a place to another
        elif "direction" in query:
            speak("tell me the starting point, Sir. Where From I have to direct")
            query = takeCommand()
            source = query
            speak("Now tell me the destination sir")
            query = takeCommand()
            destination = query
            webbrowser.open("https://www.google.com/maps/dir/"+source+"/"+destination)
            speak("Now, I'm showing you the direction sir")

        elif "what is my ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
        elif "open command prompt" in query:
            os.system("start cmd")    
