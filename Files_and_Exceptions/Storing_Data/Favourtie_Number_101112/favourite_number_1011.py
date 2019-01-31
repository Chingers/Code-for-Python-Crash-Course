#10-11, Python Crash Course, Favourite Number

import json

#Prompts user for their favourite number and save it into a json file

filename = "fav_num.json"

favNum = input("What is your favourite number? ")

with open(filename, "w") as fileObj:
    json.dump(favNum, fileObj)
    print("We have rememberd your number!")

    
