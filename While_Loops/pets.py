#Removing all indtances of a specific value from a lisr

#stores pets in a list and print the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

#Will remove all instances of cat from the list
while "cat" in pets:
    pets.remove('cat')

print(pets)
