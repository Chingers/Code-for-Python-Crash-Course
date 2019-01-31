#User Input and While Loops, Using Breaks

#The 'break' statement can be used in any loop

#Prompt
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\nEnter 'quit' to end the program: "

#prints the users input back to the user until the user breaks out of loop
while True: #endless loop until broken out of using break
    city = input(prompt)

    if city == "quit":
        break #Stops executing the rest of code in loop and exits loop
    else:
        print("\nI'd love to visit " + city.title() + ".")
