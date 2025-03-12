import pyttsx3
import platform

def speak(text):
    """Speaks the given text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Mukesh")
    while True:
        x = input("Enter what you want to speak: ")
        if x.lower() == "exit":
            speak("bye bye from RoboSpeaker")
            break
        speak(x)



