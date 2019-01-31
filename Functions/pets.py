#Positional/Keyword Arguements/Default Values, Order Mattes

def describe_pet(petName= "FORGOT", animalType= "dog", ): #Defines function, 
    """Displays information about a pet""" #Docstring
    print("I have a " + animalType + "." +
          "\nMy " + animalType + "'s name is " + petName.title() + ".")

#Function call 
describe_pet(petName= "willie", animalType= "dog") #Positional
describe_pet("Jacko") #Positional/Using Default Value
describe_pet(petName= "harry",animalType= "hamster") #Keyword
describe_pet()

#Remeber that when using default values always try listing the
#default values after all the other parameters. This allows Python
#to contonue interpreting the positional arguements correctly
