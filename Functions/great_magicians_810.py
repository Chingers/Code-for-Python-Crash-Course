#8-10, Python Crash Course, Great Magicians

#Functions
def make_great(magicians):
    """Adds the phrase ' the Great at the end of every magicians name"""
    index = 0
    while index < len(magicians):
        magicians[index] += " the Great."
        index += 1
        
def show_magicians(magicians):
    """Prints names of all magicians in list"""
    for magician in magicians:
        print(magician.title())

#BODY

#Variables
magicians = ['david blaine', 'ramsey', 'shin lim', 'jibrizy',]

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
