#4-7, Python Crash Course, mulitples of three

#list comprehension
multiplesThree = [num*3 for num in range(3,31)]
for multiple in multiplesThree:
    print(multiple)
print("\nCheck:")

check = [x/3 for x in multiplesThree]
for quotient in check:
    print(int(quotient))
