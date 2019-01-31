#74, Python Crash Course, Pizza Toppings

#prompt
prompt = "\nEnter one pizza topping you would like to add?"
prompt += "\nEnter 'quit' once you are done adding toppings: "

#Asks for toppings and displays message while message is not 'quit'
while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print("\nAdding " + topping.lower() + " to your pizza!")
