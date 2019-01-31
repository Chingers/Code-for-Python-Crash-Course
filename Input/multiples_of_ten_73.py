#7-3, Python Crash Course, Multiples of Ten

#Stores the prompt for user innput
prompt = "Give me a number, and I will tell you if it is a multiple of 10: "

#Stores user's number in variable
number = int(input(prompt))

#Checks if number is a multiple of ten and displays a message
if number % 10 == 0:
    print("\nThe number " + str(number) + " is indeed a mulitple of 10. ")
else:
    print("\nThe number " + str(number) + " is not a mulitple of 10. ")
