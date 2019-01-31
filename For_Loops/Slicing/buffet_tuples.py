#4-13, Python Crash Course, Tuples

foods = ('steak', 'pizza', 'chicken')

for food in foods:
    print(food.title())

print("\nWhooops, the menu has changed: ")
foods = ('fish and chips', 'pizza', 'chicken')

for food in foods:
    print(food.title())
