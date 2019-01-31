#Changes a value of an element in a list

motorcycles = [] #creates the list, it is currently empty
print(motorcycles)

#motorcycles[0] = 'ducati' #changes the value of an element at the given index
motorcycles.append('honda') #adds alement to end of list
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati') #inserts element and given index and shifts all other elements to the right
print(motorcycles)

del motorcycles[0] #delete's element at index 0, can remove item at any index in list
print(motorcycles)

poppedMotorcycle = motorcycles.pop() #if no parameters are given it pops last item on list out, but you can give an index
print(motorcycles)
print(poppedMotorcycle)

print(motorcycles)
firstMotorcycle = motorcycles.pop(0) #Popping is good for when you want to delete something off a list and still use it
print("The first motor cycle in my list is " + firstMotorcycle.title() + ".")

motorcycles = []
motorcycles.append('honda') #adds alement to end of list
motorcycles.append('yamaha')
motorcycles.append('suzuki')
expensive = 'honda'
print(motorcycles)
motorcycles.remove(expensive)
print("\nA " + expensive.title() + " motorcycle is was too expensive to be on this list.\n")
