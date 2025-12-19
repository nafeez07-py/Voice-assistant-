import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            said = r.recognize_google(audio)
            return said.lower()
        except Exception as e:
            print("Exception: " + str(e))
            return ""


while True:
    text = get_audio()
    if not text:
        continue
    
    if "hi" in text or "hello" in text:
        speak("Hello! How can I help you?")
    
    if "good morning" in text:
        speak("Good morning! How are you today?")
    
    if "how are you" in text:
        speak("I'm doing well, thank you for asking!")
    
    if "what is your name" in text or "who are you" in text:
        speak("My name is Frido, your voice assistant.")
    
    if "open calculator" in text:
        os.system("calc")
        speak("Opening Calculator")
    
    if "open chrome" in text:
        webbrowser.open("microsoft-edge://")
        speak("Opening Microsoft Edge")
    
    if "open youtube" in text:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    
    if "wikipedia" in text or "tell me about" in text:
        query = text.replace("wikipedia", "").replace("tell me about", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find information on that topic.")
    
    if "exit" in text or "quit" in text or "bye" in text:
        speak("Goodbye! Have a great day!")

        break
