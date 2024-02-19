import random
import json
from SpeakAndListen import speak, takeCommand, wakeCommand
import torch
from model import NeuralNet
from chat import myassistant
from nltk_utils import bag_of_words, tokenize
from sendmail import sendEmail, addEmail, mymailerfunc
from homeautomation import homeAutomationfunc
from dateandTime import dateandtimefunc
from searchwikipedia import searchwikipediafunc
from websearch import searchgooglefunc, callgooglesearch
from youtubesearch import searchyoutubefunc, searchyoutube

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents2.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data2.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def wakeup():
    #wakeuplist = ['hey bot', 'wake up', 'hello bot', 'start', 'bot','wake up bot']
    #say = input("Say: ")
    print("Say Now")
    say = input("Say: ")
    # say = input()
    # say = wakeCommand().lower()
    say = tokenize(say)
    X = bag_of_words(say, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    print(prob.item())
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                speak("Hello I am online")
                eval(response)  # print response
    else:
        print("Idk")
        wakeup()
    # while True:
    #     for i in range(len(wakeuplist)):
    #         if say == "hey bot" or say == "bot" or say == "hello bot" or say == "wake up":
    #             speak("Hello I am online")
    #             print("Hello I am online")
    #             myassistant()
    #             return
    #         else:
    #             print("Idk")
    #             wakeup()
wakeup()