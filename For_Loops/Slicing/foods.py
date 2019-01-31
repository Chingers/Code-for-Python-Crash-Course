#Copying a list, Copying a list using slice creates an entirely new one avoiding aliasing issues

myFoods = ['pizza', 'chicken', 'pork']
friendsFoods = myFoods[:]

print("my favourite foods are:")
print(myFoods)

print("\nMy friends favourite foods are:")
print(friendsFoods)


