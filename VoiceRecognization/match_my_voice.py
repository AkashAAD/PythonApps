import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os, sys, subprocess

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[11].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")
  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")
  else:
    speak("Good Evening!")

  speak("I am Jarvis Sir. Please tell me how may I help you!")


def takeCommand(): # It takes microsoft imput from user and returns string output
  r  = sr.Recognizer() 
  with sr.Microphone() as source:
    print("Listning...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language="en-in")
    print(f"User said: {query}\n")
  except Exception as e:
    print(e)
    print("Say that again please")
    return "None"
  return query

if __name__ == "__main__":
  wishMe()
  while True:
    query = takeCommand().lower()
    # import pdb; pdb.set_trace()
    if 'wikipedia' in query:
      speak("Searching wikipedia...")
      query     = query.replace("wikipedia", "")
      resultes  = wikipedia.summary(query, sentences=2)
      speak("According to wikipedia")
      print(resultes)
      speak(resultes)
    elif "open youtube" in query:
      webbrowser.open("youtube.com")
    elif "open google" in query:
      webbrowser.open("google.com")
    elif "open stackoverflow" in query:
      webbrowser.open("stackoverflow.com")            
    elif "play music" in query:
      dirs = "/home/akash/Desktop/Python Apps/VoiceRecognization"
      files = os.listdir(dirs)
      opener = "open" if sys.platform == "linux" else "xdg-open"
      subprocess.call([opener, os.path.join(dirs, files[1])])
      # os.startfile(os.path.join(dirs, files[1]))
    elif "the time" in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      print(strTime)
      speak(f"Sir, The time is {strTime}")
