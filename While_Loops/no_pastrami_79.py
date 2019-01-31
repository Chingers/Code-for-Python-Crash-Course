#7-9, Python Crash Course, No Pastrami

#Stores orders
sandwichOrders = ["tuna", "pastrami", "pastrami", "ham", "pastrami", "BLT",
                  "egg salad", "turkey"]
finishedOrders = []

#Prints orders
print("Orders: " + str(sandwichOrders))
#Alerts users that deli has run out of pastrami
print("\nSorry, We have run out pastrami!\n")

#Removes all instances of pastrami from sandwichOrders
while "pastrami" in sandwichOrders:
    sandwichOrders.remove("pastrami")

#Verifies that the sandwich is made and moves items to finishedOrders
while sandwichOrders:
    #Pops last sandwich in sandwich list in variable
    sandwich = sandwichOrders.pop()
    #Adds sandwich into finishedOrders list
    finishedOrders.append(sandwich)
    
    #Verify that sandwhich was made
    print("I made your " + sandwich + " sandwich.")

#Displays all finished sandwiches
print("\n--Finished Sandwiches--")
for order in finishedOrders:
    print(order + " sandwich.")
