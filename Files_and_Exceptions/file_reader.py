#Reads from a text file

fileName = "pi_digits.txt"

#Opens the file and prints each line
with open(fileName) as fileObject:
    for line in fileObject:
        print(line.rstrip())In 

#Opens the file and stores each line in list
with open(fileName) as fileObject2:
    lines = fileObject2.readlines()

#Prints each line in the list
for line in lines:
    print(line.rstrip())
