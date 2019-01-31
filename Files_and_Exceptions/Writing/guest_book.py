#10-4, Python Crash Course, Guest Book

filename = "guest_book.txt"
guests = []

while True:

    with open(filename) as fileObject:
        for line in fileObject:
            guestName = line.strip()
            guests.append(guestName.title())
    
    name = input("Name (Enter 'q'): ")
    if (name == 'q'):
        break
    elif (name.title() in guests):
        print("You are already on the guest list.")
    else:
        print("You have been added to the guest list.")
        with open(filename, "a") as fileObject:
            fileObject.write(name.title() + "\n")
