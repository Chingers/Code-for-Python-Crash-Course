#8-11, Python Crash Course, Unchanged Magicians

#Functions
def make_great(magicians, greatMagicians):
    """
    Adds the phrase ' the Great at the end of every magicians name
    while saving the original list and creating a new one with the phrase
    """
    while magicians:
        magician = magicians.pop()
        magician += " the Great"
        greatMagicians.append(magician)
                
def show_magicians(magicians):
    """Prints names of all magicians in list"""
    for magician in magicians:
        print(magician.title())

#BODY

#Variables
magicians = ['david blaine', 'ramsey', 'shin lim', 'jibrizy',]
greatMagicians = []

make_great(magicians[:], greatMagicians) #Passes copy of list to prevent alias
show_magicians(magicians)
show_magicians(greatMagicians)
