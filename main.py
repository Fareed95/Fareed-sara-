import speech_recognition as sr
import pyttsx3 
import webbrowser 


r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get and list available voices
voices = engine.getProperty('voices')


# Set the desired voice
# For example, let's select the second voice in the list (index 1)
engine.setProperty('voice', voices[1].id)

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open linkedin" or "open my linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" or "open my github" in command.lower():
        webbrowser.open("https://www.github.com")
    elif "open telegram" in command.lower():
        webbrowser.open("https://www.telegram.com")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Sara, Activated ...")
    while True:
    # listen for the wake up word 
        r = sr.Recognizer()
        print("recognizing")
        # recognize speech using Sphinx
        try:    
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                print("recognizing")
            word = (r.recognize_google(audio))
            print(word)
            if "sara" in word.lower():
                speak("YES,SIR ?")
                with sr.Microphone() as source:
                    print("Listning.....")
                    audio = r.listen(source,timeout=2)
                    print("recognizing")
                    command = (r.recognize_google(audio))
                    print(command)
                    processCommand(command)
        except Exception as e :
            print(e)
