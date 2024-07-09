import speech_recognition as sr

while True:
    # listen for the wake up word 
        r = sr.Recognizer()
        # print("recognizing")
        # recognize speech using Sphinx
        try:    
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source,timeout=2)
            print("recognizing")
            word = (r.recognize_google(audio))
            print(word)

        except Exception as e :
            print(e)