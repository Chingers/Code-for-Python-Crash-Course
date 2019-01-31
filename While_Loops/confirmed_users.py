#Using while loops with dictionaries and lists

#Start with storing the users that need to be verifies
unconfirmedUsers = ['alice', 'brian', 'candace']

#Stores list of confirmed users
confirmedUsers = []

#Verify each user until there are no more un verfied users left
#Move all verified users to the confirmed list
while unconfirmedUsers:
    #Gets last user in list and pops it into the currentUser variable
    currentUser = unconfirmedUsers.pop()

    print("Verifying user: " + currentUser.title())
    confirmedUsers.append(currentUser)

#Display all confirmed users
print("\nThe following users have been confirmed:")

for confirmedUser in confirmedUsers:
    print(confirmedUser.title())
