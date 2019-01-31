#Nested Dictionaries and lists

#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens and store in list
for alienNum in range(30):
    newAlien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(newAlien)

#Change characteristics of aliens
for alien in aliens[:3]:
    if (alien["colour"] == "green"):
        alien["colour"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif (alien["colour"] == "yellow"):
        alien["colour"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
#Show first five aliens
for alien in aliens[:5]:
    print(alien)

print("...")

#Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
