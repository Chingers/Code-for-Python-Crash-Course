#Working with classes and instances

#Creates class
class Car():
    """A simple attempy to represent a car"""

    #Initializes attributes
    def __init__(self, make, model, year):
        """Initializes attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

        
    def get_descriptive_name(self):
        """Resturns a neatly formatted descriptive name"""
        longName = str(self.year) + " " + self.make + " " + self.model
        return longName.title()


    def read_odometer(self):
        """Prints statement showing the car's mileage"""
        print("This car has " + str(self.odometerReading) + " miles on it.")


    def update_odometer(self, mileage):
        """
        Sets the odometer reading to given value
        Rejects change if it will mae odometer roll back
        """

        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back the odomoter reading dummy.")


    def increment_odometer(self, miles):
        """
        Adds the given amount to the odometer reading
        Rejects negative increments
        """
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't roll back the odomoter reading dummy.")

            
               #Make  #Model #Year
myNewCar = Car("audi", "a4", 2016)
print(myNewCar.get_descriptive_name())

myNewCar.update_odometer(23)
myNewCar.read_odometer()
myNewCar.increment_odometer(100)
myNewCar.update_odometer(23)
myNewCar.read_odometer()
