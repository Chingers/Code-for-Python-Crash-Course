#7-5, Python Crash Course, Movie Tickets

#Prompt
prompt = "\nWhat is your age?"
prompt += "\nEnter 'quit' once you are done: "

#Stores value for flag
flag = True

#Stores movie ticket price
price = 0

#While loop
while flag:
    age = input(prompt)

    if age == 'quit': #Always put break events first
        break

    #Type casts age as a integer
    age = int(age)

    #Assings appropriate price for movie ticket
    if age == 3:
        price = 0
    elif (age > 3) and (age <= 12):
        price = 10
    elif age > 12:
        price = 15

    print("\nThe cost of your movie ticket is $" + str(price))
        
