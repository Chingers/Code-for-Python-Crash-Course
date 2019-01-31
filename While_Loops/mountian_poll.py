#Filling a Dictionary with User Input

#stores dictionary of responses, key: name, value: response
responses = {}

#Flag
pollActive = True

while pollActive:
    #Prompt user for name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Creates a new key-value pair in dictionary
    responses[name] = response

    #Find out if anyome else is going to take the pole
    repeat = input("\nWould you like another person to repond? (yes/no)")
    if repeat == "no":
        pollActive = False

#Show results of poll
print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
