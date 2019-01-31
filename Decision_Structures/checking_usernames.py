#5-10, Python Crash Course, Checking Usernames

currentUsers = ['mark', 'kyle' , 'bachels', 'monching', 'connor']
newUsers = ['falahafomisa', 'ski mask' , 'bachels', 'mOnching', 'KYLE']
tempCurrentUsers = [] #Temporary list that holds all names in lowercase

for currentUser in currentUsers:
    tempCurrentUsers.append(currentUser.lower()) #adds lowerscase names to list

for newUser in newUsers: #Loops through every element in new Users
    if newUser.lower() in tempCurrentUsers: #checks if new username exists
        print("You can't use that username.")

    else:
        print("That username is available.") 
