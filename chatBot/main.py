from chatBot.SpeakAndListen import speak, takeCommand, wakeCommand
from chatBot.chat import myassistant


def wakeup():
    wakeuplist = ['hey bot', 'wake up', 'hello bot', 'start', 'bot','wake up bot']
    # say = input("Say: ")
    print("Say Now")
    # say = wakeCommand().lower()
    say = input("Say: ")
    while True:
        for i in range(len(wakeuplist)):
            if say == "hey bot" or say == "bot" or say == "hello bot" or say == "wake up":
                # speak("Hello I am online")
                print("Hello I am online")
                myassistant()
                return
            else:
                print("Idk")
                wakeup()