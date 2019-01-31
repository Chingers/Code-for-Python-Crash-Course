#10-6/10-7, Python Crash Course, Addition

while True:
    #Displays instructions
    print("Provide me wiht two integers and I will be able to add them." +
          "\n(Enter 'q' to exit the program.)")
    #Prompts user for first number
    firstNum = input("First Number: ")
    #Checks if user wants to exit
    if (firstNum == 'q'):
        break
    
    #Prompts user for second number
    secondNum = input("Second Number: ")
    #Checks if user wants to exit
    if (secondNum == 'q'):
        break
    
    #Try's adding number
    try:
        answer = int(firstNum) + int(secondNum)
    except ValueError:
        print("Please input integers only!\n")
    else:
        #Prints added numbers
        print("The sum of your two number is " + str(answer) + ".\n")
