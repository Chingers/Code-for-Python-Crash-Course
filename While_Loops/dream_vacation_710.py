#7-10, Python Crash Course, Dream Vacation

#Stores responses from users
responses = {}

while True:
    #Prompt Users
    name = input("What is your name? ")
    response = input("Where would your dream vacation be? ")

    #Puts key-value pair in dictionary
    responses[name] = response

    #Verfies if the users want to continue with poll
    repeat = input("\nWould you like to continue the poll (yes/no)? ")
    if repeat == "no":
        break

#Prints Poll Results
print("\n--Poll Results--")
for name, response in responses.items():
    print(name.title() + "'s dream vacation would be to " + response)
    
