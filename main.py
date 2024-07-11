import speech_recognition as sr
from processcommand import processCommand,speak,microphone


if __name__ == "__main__":
    speak("Saara! Activated ...")
    while True:
        try:    
            word = microphone(2)
            if "sara" in word.lower():
                while True :
                    speak("YES,SIR ?")
                    command = microphone(5)
                    print("recognizing")
                    print(command)
                    processCommand(command)
                    if "ok thanks" in  command.lower() or command.lower()=="thankypu":
                        speak("If require any help, please call me again.")
                        break
                    
        except Exception as e :
            print(e)
