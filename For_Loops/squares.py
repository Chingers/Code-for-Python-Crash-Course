#Outputing the squares of the first ten numbers using range

squares = []

for value in range(1,11):
    squared = value**2
    squares.append(value**2)
print("Squares: " + str(squares))

print("\nSmallest: " + str(min(squares)) + "\nBiggest: " + str(max(squares)) + "\nSum: " + str(sum(squares)))

cubes = [value**3 for value in range(1,11)] #Uses lists comprehension to generate a list of the cubic values of the first tenposotive integers
print("Cubes: " + str(cubes))
