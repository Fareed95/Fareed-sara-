import speech_recognition as sr
import pyttsx3 
import webbrowser 
import musicplayer
from volume import increase_volume, decrease_volume
from text_remover import text_remover_mummy,text_remover,text_remover_search
from file_saver import file_saver,file_saver_bot
import os 
from bot_algo import bot_gemini


r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def microphone(phrase_time_limit):
    try:
        with sr.Microphone(device_index=1) as source:
            print("Listening.....")
            audio = r.listen(source, timeout=2, phrase_time_limit=phrase_time_limit)
        word = r.recognize_google(audio)
        print("Recognizing...")
        print(word)
        return word
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""



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
        webbrowser.open("https://web.telegram.org/a/")

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
        file_saver(r'/home/fareed-sayed/Documents/MERI SAARA/','mummy_work.txt',text_remover_mummy(command.lower()))
        speak(f"Noted! {text_remover_mummy(command.lower())} in mummy_work.txt")
        
    elif "note" in command.lower():
        file_saver(r'/home/fareed-sayed/Documents/MERI SAARA/','important_work.txt',text_remover(command.lower()))
        speak(f"Noted! {text_remover_mummy(command.lower())} in important_work.txt")
    elif "file explorer" in command.lower():
        explorer_path = "C:\\Windows\\explorer.exe"
        speak("Opening file explorer")
        os.startfile(explorer_path)
    elif "want to ask"in command.lower()  or "want to know" in command.lower():
        speak("Yes sir, please ?")
        question = microphone(7)
        print("recognizing")
        print(question)
        speak("Do you want me to just write it or you also want to know about it ?")
        asking_saara = microphone(5)
        if "just" in asking_saara.lower() and "write" in asking_saara.lower():
            speak("Done ")
            file_saver_bot(question,bot_gemini(question))
        else :
            bot_answer = bot_gemini(question)
            file_saver_bot(question,bot_answer)
            speak(bot_answer)


        
if __name__ == "__main__":
    microphone(5)
    # pass