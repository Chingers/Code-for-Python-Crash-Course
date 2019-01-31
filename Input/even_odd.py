#Using Modulo, For Python 2.7 use "raw_input()"

#Gets user's number and stores it in variable
number = input("Enter a number, and I'll tell you if it's even or odd: ")
#Type casts the string number into an integer
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even!")
else:
    print("\nThe number " + str(number) + " is odd!")

