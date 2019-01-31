#Module for Pizza Program

def make_pizza(size, *toppings): #Asterix makes empty tuple to store arguements 
    """Prints the list of toppings that have been requested"""
    print("\nMaking a " + str(size) + "-inch " +
          "pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


