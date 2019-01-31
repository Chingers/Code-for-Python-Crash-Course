#Using  while loop to count up to the number 5

#Stores current number
currentNum = 0

#Prints the odd numbers from one to ten
while currentNum < 10:
    #What you do to all numbers
    currentNum += 1

    #Checks if number is even
    if currentNum % 2 == 0:
        continue #Continues to beginning loop and does not print even number

    #What you do to the odd number only
    print(currentNum)    
    
