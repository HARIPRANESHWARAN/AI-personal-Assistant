import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set speech rate and volume
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except Exception as e:
        print("Sorry, I could not understand your command. Please try again.")
        return None

# Function to wish the user based on the time of day
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am your personal assistant. How can I help you today?")

# Function to perform tasks based on voice commands
def execute_task(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {time}")
        
    elif 'date' in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {date}")
        
    elif 'search' in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query} on Google.")
        kit.search(query)
        
    elif 'play' in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        kit.playonyt(song)
        
    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        speak(f"Searching Wikipedia for {query}")
        summary = wikipedia.summary(query, sentences=1)
        speak(summary)
        
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        
    elif 'open' in command:
        if 'browser' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening your web browser.")
        elif 'notepad' in command:
            speak("Opening Notepad.")
            kit.playonyt("open notepad")  # Use a command for Notepad or any program you'd like to open
            
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

# Main function to run the assistant
def main():
    wish_user()
    
    while True:
        command = listen()
        if command:
            execute_task(command)

if __name__ == "__main__":
    main()
