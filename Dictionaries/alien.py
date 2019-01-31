#Dictionaires, Use 'del' to delete a key and its value from the dictionary

alien0 = {'xPosition': 0, 'yPosition': 25, 'speed': 'medium'}

print("Original x position: " + str(alien0["xPosition"]))

if alien0['speed'] == 'slow':
    xIncrement = 1

elif alien0['speed'] == 'medium':
    xIncrement = 2

else:
    xIncrement = 3

alien0['xPosition'] = alien0['xPosition'] + xIncrement

print("New x position: " + str(alien0["xPosition"]))
