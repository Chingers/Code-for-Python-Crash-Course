#10-13, Python Crash Course, Favourite Number Remembered

import json

#Loads the users favourite number if available
#If not, then the program will prompt the suer for favourite nuumber


def get_fav_num():
    """Will retrieve users favourite number if available"""
    in_filename = "fav_num.json"
    
    try:
        with open(in_filename, "r") as fileObj:
            favNum = json.load(fileObj)
    except FileNotFoundError:
        return None
    else:
        return favNum


def ask_fav_num():
    """Prompts user for their favourite number and stores it"""
    in_filename = "fav_num.json"
    
    favNum = input("What is your favourite number? ")
    with open(in_filename, "w") as fileObj:
        json.dump(favNum, fileObj)

def tell_fav_num():
    """Tells user their favourite number"""

    in_filename = "fav_num.json"
    favNumRead = get_fav_num()
    if favNumRead:
        print("Your favourite number is " + favNumRead + "!")
    else:
        ask_fav_num()
        print("We have rememberd your number!")
        

tell_fav_num()
