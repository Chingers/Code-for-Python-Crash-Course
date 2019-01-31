#9-1, Python Crash Course, Restaurant
#Defines a class named restaurant and calls methods in the class

#Class Definition
class Restaurant():
    """A simple attempt to represent a restaurant"""

    #Initialize attributes
    def __init__(self, name, cuisineType, numServed=0):
        """Initializes attributes to describe restaurant"""
        self.name = name;
        self.cuisineType = cuisineType;


    def describe_restaurant(self):
        """Return's a neatly formatted description of the restaurant"""
        print("The name of this restaurant is " + self.name.title() +
              " and it's cuisine type is " + self.cuisineType.title() + ".")


    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print("The restaurant " + self.name.title() + " is now open!")


#BODY
restaurant = Restaurant("something sweet", "filipino") #Creates instance
restaurant2 = Restaurant("pho mi", "vietnamese")
restaurant3 = Restaurant("Osmow's", "mediterranean")

print(restaurant.name)
print(restaurant.cuisineType)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
