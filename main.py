import speech_recognition as sr
import pyttsx3 
import webbrowser 
import musicplayer
from volume import increase_volume, decrease_volume
from text_remover import text_remover_mummy,text_remover,text_remover_search
from file_saver import file_saver
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

    elif "search for" in command.lower():
        text = text_remover_search(command.lower())
        speak(f"Searching for {text} in google")
        words = text.split()  # Split the text into words
        result = '+'.join(words)  # Join the words with '+'
        # print(result)
        webbrowser.open(f"https://www.google.com/search?q={result}")

    elif "open linkedin" in command.lower() or "open my linkedin" in command.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "search in youtube" in command.lower():
        text = text_remover_search(command.lower())
        speak(f"Searching for {text} in youtube")
        words = text.split()  # Split the text into words
        result = '+'.join(words)  # Join the words with '+'
        # print(result)
        webbrowser.open(f"https://www.youtube.com/results?search_query={result}")

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

    elif "note" in command.lower() and "mummy" in command.lower():
        file_saver(r'C:\Users\Admin\OneDrive - RizviCollegeOfEngineering\Documents\Saara documents','mummy_work.txt',text_remover_mummy(command.lower()))
        speak(f"Noted! {text_remover_mummy(command.lower())} in mummy_work.txt")
        
    elif "note" in command.lower():
        file_saver(r'C:\Users\Admin\OneDrive - RizviCollegeOfEngineering\Documents\Saara documents','important_work.txt',text_remover(command.lower()))
        speak(f"Noted! {text_remover_mummy(command.lower())} in important_work.txt")
        

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Saara! Activated ...")
    while True:
    # listen for the wake up word 
        r = sr.Recognizer()
        # print("recognizing")
        # recognize speech using Sphinx
        try:    
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
                print("recognizing")
            word = (r.recognize_google(audio))
            print(word)
            if "sara" in word.lower():
                while True :
                    speak("YES,SIR ?")
                    with sr.Microphone() as source:
                        print("Listning.....")
                        audio = r.listen(source,timeout=2,phrase_time_limit=5)
                        print("recognizing")
                    command = (r.recognize_google(audio))
                    print(command)
                    processCommand(command)
                    if "ok thanks" in  command.lower() or command.lower()=="thankypu":
                        speak("If require any help, please call me again.")
                        break
                    
        except Exception as e :
            print(e)
