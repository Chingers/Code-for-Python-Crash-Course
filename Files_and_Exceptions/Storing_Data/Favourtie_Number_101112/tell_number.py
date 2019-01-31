#10-11, Python Crash Course, Tells user their favourite number

import json

filename = "fav_num.json"

with open(filename, "r") as fileObj:
    favNumRead = json.load(fileObj)
    print("Your favourite number is " + favNumRead + "!")
