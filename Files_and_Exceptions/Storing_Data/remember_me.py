#Saving and reading user generated data

import json

#Loads username, if it had been stored already
# Otherwise, prompt for the username and store it

def get_stored_username():
    """Gets stored username if available"""

    filename = "username.json"

    try:
        with open(filename, "r") as fileObj:
            username = json.load(fileObj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Gets a username from the user and stores it in json file"""
    username = input("What is you username? ")
    filename = "username.json"
    with open(filename, "w") as fileObj:
        json.dump(username, fileObj)
    return username


def greet_user():
    """Greets user by name."""

    response = ""
    answers = ["Y", "N"]
    username = get_stored_username()
    if username:
        while response not in answers:
            response = input("Is '" + username + "' your username? " +
                             "\n(Enter 'Y' or 'N'): ")
            
        if response == 'Y':
            print("Welcome back " + username + "!")
        else:
            username = get_new_username()
            print("We will remember you when you return " + username + "!")          
    else:
        username = get_new_username()
        print("We will remember you when you return " + username + "!")
    

greet_user()
