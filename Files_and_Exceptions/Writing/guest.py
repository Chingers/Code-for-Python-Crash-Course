#10-3, Pytthon Crash COurse, Guest

name = input("Input your name: ")

filename = "guest.txt"

with open(filename, "w") as fileObject:
    fileObject.write(name)    
