import speech_recognition as sr         #modules
import pyttsx3     # python text to speech
import pywhatkit  # contain a youtube function which plays music
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()           #engine require to talk for alexa
voices = engine.getProperty('voices')  # different voice of male/female
engine.setProperty('voice', voices[2].id)


def talk(text):     #create a talk function
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)    #listen your voice with the help of google api
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is the' in command:
        person = command.replace('who is the', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'feeling' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'shut down' in command:
        talk('shutting down...')
        breakpoint()
    else:
        talk('Please say the command again.')
while True:
    run_alexa()