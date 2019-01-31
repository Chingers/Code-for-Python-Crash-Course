#Inheritance, Always make sure parent classes are defined before child classes.

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

#Battery Class
class Battery():
    """A simple attempt to model a battery of an electric car"""

    def __init__(self, batterySize=70):
        """Initializes batteries attributes."""
        self.batterySize = batterySize


    def describe_battery(self):
        """Prints a statement describing battery size"""
        print("This car has a " + str(self.batterySize) + "-kWh battery.")


    def upgrade_battery(self):
        """Upgrades battery to 85-kWh if it already isnt"""
        if self.batterySize != 85:
            self.batterySize = 85
            
        print("Battery Has been update to 85-kWh.")


    def get_range(self):
        """Prints a statement about the range that the battery provides."""
        if (self.batterySize == 70):
            batRange = 240
        elif (self.batterySize == 85):
            batRange = 270

        print("This car can go approximately " + str(batRange) +
              " miles on a full charge.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initializes attributes to parent class
        The initializes the attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def describe_battery(self):
        """Prints a statement describing battery size."""
        print("This car has a " + str(self.batterySize) + "-kWh battery.")

    
    def fill_gas_tank(self):
        """Electric cars done have gas tanks"""
        print("this car doesn't need a gas tank!")


myTesla = ElectricCar("tesla", "model s", 2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describe_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()
myTesla.battery.get_range()
