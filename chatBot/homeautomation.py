import random
import json
from chatBot.SpeakAndListen import speak, takeCommand
import torch
from chatBot.model import NeuralNet
from chatBot.nltk_utils import bag_of_words, tokenize
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

bot_name = "AVAYA"
def homeAutomationfunc():
    print("I am in home automation")
    with open('intents1.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "./assets/models/data1.pth"
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

    while(1):
        homeAutomationinput = input("You: ")  # This is used to text based input
        #homeAutomationinput = takeCommand().lower()      #this is voice based input
        homeAutomationinput = tokenize(homeAutomationinput)
        X = bag_of_words(homeAutomationinput, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]
        print(tag)
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        print(prob.item())
        if prob.item() >= 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    response = random.choice(intent['responses'])
                    print(f"{bot_name}: {response}")  # this is text based output
                    # speak(response)                                     #this is voice based output
        else:
            # speak("I do not understand")
            print(f"{bot_name}: I did Not understand...")
            print("Switching to Chatbot mode")
            return
        for intent in intents['intents']:
            if tag != intent["tag"]:
                continue
            print(tag)
            print("You can try saying?")
            print(intent['patterns'])

