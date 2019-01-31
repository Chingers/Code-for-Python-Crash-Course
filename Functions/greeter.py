#Defining a function

def greet_user(username): #Function Definition, username is a parameter
    """Displays a simple greeting.""" #A docstring
    print("Hello " + username.title() + "!")

def get_formatted_name(firstName, lastName, middleName= ""):
    """Returns a full name, neatly formatted"""

    if middleName:
        fullName = firstName + " " + middleName + " " + lastName
    else:
        fullName = firstName + " " + lastName
        
    return fullName.title() #Returns the value to the line

#greet_user("Monching") #"Monching" is an arguement

#Infinite loop!
while True:
    print("\nPlease tell me yuor name (Enter 'q' at anytime to quit):")
    fName = input("First Name: ")
    if fName == "q":
        break
    
    lName = input("Last Name: ")
    if lName == "q":
        break
    
    print("\nHello, " + get_formatted_name(fName,lName) + "!")
