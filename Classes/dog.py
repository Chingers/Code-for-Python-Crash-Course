#Creating a Class

#Class Definition
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age): #A method 
        """Initialize name and age attributes."""
        self.name = name #self.name (name is considered an attribute)
        self.age = age


    def sit(self):
        """Simulates dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """Simulates rolling over in responese to a command."""
        print(self.name.title() + " rolled over!")


#BODY

#Creating an instance of a class
myDog = Dog("willie", 6)
yourDog = Dog("lucy", 3)

#My Dog
print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old.")
myDog.sit()
myDog.roll_over()
#Your Dog
print("\nYour dog's name is " + yourDog.name.title() + ".")
print("Your dog is " + str(yourDog.age) + " years old.")
yourDog.sit()
