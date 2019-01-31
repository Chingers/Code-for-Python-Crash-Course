#Using json module to read a data structure from a json file

import json

filename = "numbers.json"

with open(filename, 'r') as fileObj:
    numbers = json.load(fileObj)

for number in numbers:
    print(number)
