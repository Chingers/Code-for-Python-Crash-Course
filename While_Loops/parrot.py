#User Input and While Loops

#Prompt
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

#Stores users input
message = ""

#Stores value for the flag of the while loop
flag = True

#prints the users input back to the user until user types 'quit'
while flag:
    message = input(prompt)

    if message == "quit":
        flag = False
    else:
        print("\n" + message)
        
