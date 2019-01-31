#Using json to load data

import json

filename = "username.json"

with open(filename, "r") as fileObj:
        username = json.load(fileObj)
    
print("Welcome Back " + username + "!")
