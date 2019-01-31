#Try-Except blocks

print("Give me two integers and I'll divide them." +
      "\n(Enter 'q' to quit)")

while True:
    firstNum = input("First Number: ")
    if (firstNum.strip() == 'q'):
        break

    secondNum = input("Second Number: ")
    if (secondNum.strip() == 'q'):
        break

    try:
        answer = int(firstNum) / int(secondNum)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print("The answer is: " + str(answer))
