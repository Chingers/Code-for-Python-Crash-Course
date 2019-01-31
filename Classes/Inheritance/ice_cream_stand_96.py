#9-6, Python Crash Course, Ice Cream Stand

#Class Definition (Parent Class)
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

#Ice Cream Stand Class (Child of Restaurant)
class IceCreamStand(Restaurant):
    """A simple representation of an ice cream stand."""

    def __init__(self, name, cuisineType, flavours, numServed=0):
        """Initializes attributes of Ice cream stand instance"""
        super().__init__(name, cuisineType, numServed=0)
        self.flavours = flavours

    def show_flavours(self):
        """Prints the flavours for the ice cream stand."""
        print("This ice cream stand has these flavours: ")
        for flavour in self.flavours:
            print(flavour.title())

benAndJerries = IceCreamStand("ben and jerries",
                              "desert",
                              ["strawberry", "vanilla", "chocolate", "cashew"])
benAndJerries.show_flavours()
