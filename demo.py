import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get and list available voices
voices = engine.getProperty('voices')

# Set the desired voice with Indian accent (if available)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Adjust speech rate if necessary

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Waalayikum, Assalam!. Khayiriyet?"
speak(text)
