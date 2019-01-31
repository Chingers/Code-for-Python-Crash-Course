#8-3/8-4, Python Crash Course, T-Shirt

#Define Funtion
def make_shirt(size = "large", message= "Monching is Cool"):
    """Displays information about T-Shirt"""
    print("The size of your shirt is " + str(size) +
          "\nMessage: " + message)

#Positional Call
make_shirt(14, "I love Python")

#Keyword call
make_shirt(size= 12)

make_shirt()
make_shirt(size= "medium")

