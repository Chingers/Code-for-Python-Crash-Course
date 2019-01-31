#This program will generate insults

#imports random and guizero library
import random
from guizero import App, Text, PushButton

#Creates the three lists
listA = []
listB = []
listC = []

#Opens, reads and returns the contents of the file

with open("insults.csv", "r") as f:
    for x in f:
        words = x.split(",")
        listA.append(words[0])
        listB.append(words[1])
        listC.append(words[2].strip())

#Funtions
def insult_me():
    wordA = random.choice(listA)
    wordB = random.choice(listB)
    wordC = random.choice(listC)
    insult = "Thou " + wordA + " and " + wordB + " " + wordC
    return insult

def new_insult():
    
    message.value = insult_me()

app = App("Insult Generator!")
message = Text(app, insult_me())
button = PushButton(app, new_insult, text="Insult me again")
app.display()

