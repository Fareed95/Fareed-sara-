import speech_recognition as sr
import pyttsx3 
import webbrowser 
import musicplayer
from volume import increase_volume, decrease_volume

r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get and list available voices
voices = engine.getProperty('voices')


# Set the desired voice
# For example, let's select the second voice in the list (index 1)
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)
def processCommand(command):
    if "open google" in command.lower():
        speak("Opening google")
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in command.lower() or "open my linkedin" in command.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open github" in command.lower() or "open my github" in command.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "open telegram" in command.lower():
        speak("Opening Telegram")
        webbrowser.open("https://www.telegram.com")
    elif command.lower().startswith("play"):
        result = " ".join(command.lower().split(" ")[1:])
        speak(f"playing {result}")
        musicplayer.player(result)
    elif "increase volume" in command.lower():
        increase_volume()
        speak("Increased volume to 10%")
    elif "decrease volume" in command.lower():
        decrease_volume()
        speak("Decreased volume to 10%")
    elif "assalam walekum" in command.lower():
        speak("Waalayikum, Assalam!. Khayiriyet?")


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Saara! Activated ...")
    while True:
    # listen for the wake up word 
        r = sr.Recognizer()
        print("recognizing")
        # recognize speech using Sphinx
        try:    
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
                print("recognizing")
            word = (r.recognize_google(audio))
            print(word)
            if "sara" in word.lower():
                speak("YES,SIR ?")
                with sr.Microphone() as source:
                    print("Listning.....")
                    audio = r.listen(source,timeout=2,phrase_time_limit=3)
                    print("recognizing")
                command = (r.recognize_google(audio))
                print(command)
                processCommand(command)
        except Exception as e :
            print(e)
