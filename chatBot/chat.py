# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:26:53 2021

@author: Shubham
"""

import random
import json
from chatBot.SpeakAndListen import speak, takeCommand
import torch
from chatBot.model import NeuralNet
from chatBot.nltk_utils import bag_of_words, tokenize
from chatBot.sendmail import sendEmail, addEmail, mymailerfunc
from chatBot.homeautomation import homeAutomationfunc
from chatBot.dateandTime import dateandtimefunc
from chatBot.searchwikipedia import searchwikipediafunc
from chatBot.websearch import searchgooglefunc, callgooglesearch
from chatBot.youtubesearch import searchyoutubefunc, searchyoutube
from chatBot.note import notefunc

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("I am in Normal Mode")
def myassistant():
    with open('./assets/intents/intents.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "./assets/models/data.pth"
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

    bot_name = "AVAYA"
    print("Let's chat! (type 'quit' to exit)")

    while True:
        sentence = input("You: ")       #This is used to text based input
        #ans = sentence
        # print(ans)
        # sentence = takeCommand().lower()      #this is voice based input
        ans = sentence
        if sentence == "quit":
            break

        #print(sentence)
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    response = random.choice(intent['responses'])
                    strLen = len(response)
                    lst = strLen - 2
                    eval(response)          #print response
                    speakres = response[18:lst]
                    # speak(speakres)       #speak response
        else:
            #speak("I do not understand")
            print(f"{bot_name}: I did Not understand...")
            print("You can try saying?")
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(tag)
                    print(intent['patterns'])
            print("Or do you want google search for whatever you have said?")
            # print("Say Yes or No")
            searchans = input("Say Yes or No: ")
            if searchans == "yes":
                searchgooglefunc(ans)
            else:
                myassistant()

