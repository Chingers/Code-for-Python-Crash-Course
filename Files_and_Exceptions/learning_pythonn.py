#10-1/10-2, Python Crash Course, Learning Python

filename = "learning_python.txt"

#Opens file, reads it and prints its contents
with open(filename) as fileObject:
    contents = fileObject.read()
    print(contents + "\n")

#Opens file, loops through every line in file and prints each line
with open(filename) as fileObject:
    for line in fileObject:
        print(line.rstrip())

    print("\n")

#Opens file, stores each line in a list and prints contents outside of block
with open(filename) as fileObject:
    lines = fileObject.readlines()

for line in lines:
    print(line.rstrip())

print("\n")
#Replaces all occurences of "Python" with "Javascript"
with open(filename) as fileObject:
    contents = fileObject.read()
    newContents = contents.replace("Python", "Javascript")
    print(newContents)
