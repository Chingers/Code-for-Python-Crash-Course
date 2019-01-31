#9-4, Python Crash Course, Number Served
#Defines a class named restaurant and calls methods in the class

#Class Definition
class Restaurant():
    """A simple attempt to represent a restaurant"""

    #Initialize attributes
    def __init__(self, name, cuisineType, numServed=0):
        """Initializes attributes to describe restaurant"""
        self.name = name;
        self.cuisineType = cuisineType;
        self.numServed = numServed;


    def describe_restaurant(self):
        """Return's a neatly formatted description of the restaurant"""
        print("The name of this restaurant is " + self.name.title() +
              " and it's cuisine type is " + self.cuisineType.title() + "." +
              " The restaurant has served " + str(self.numServed) + ".")


    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print("The restaurant " + self.name.title() + " is now open!")


    def set_num_served(self, number):
        """Sets number of customers served to given number"""
        self.numServed = number


    def increment_num_served(self, increment):
        """Increments number of customers served by given value"""
        self.numServed += increment
        
      
#BODY
restaurant = Restaurant("something sweet", "filipino", 7) #Creates instance
restaurant.describe_restaurant()
restaurant.set_num_served(50)
restaurant.describe_restaurant()
restaurant.increment_num_served(5)
restaurant.describe_restaurant()

