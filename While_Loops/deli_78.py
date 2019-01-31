#7-8, Python Crash Course, Deli

#Stores orders
sandwichOrders = ["tuna", "meatball", "egg salad", "ham", "BLT"]
finishedOrders = []

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

    
