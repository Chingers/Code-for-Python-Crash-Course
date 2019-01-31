#Working with a files contents

filename = "pi_digits.txt"

with open(filename) as fileObject:
    lines = fileObject.readlines()

piString = ""
for line in lines:
    piString += line.strip()

print(piString)
print(len(piString))
