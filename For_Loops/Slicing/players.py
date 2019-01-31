#Slicing a List

players = ['charles', 'martina', 'micheal', 'florence', 'eli']

print("Here are the first three players on the team:");
for player in players[0:3]:
    print(player.title()) #Prints out elements with index's 0,1,2

#Without a starting index python automatically starts at index 0
#Omitting the second index will slice the list from the firt one to the end

