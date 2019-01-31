#Modifying a list within a function

#Imports modules/libraries
import printing_functions as pf

#BODY of program
unprintedDesigns = ['iphone case', 'robot pendant', 'dodecahedron']
compModels = []

pf.print_models(unprintedDesigns=unprintedDesigns,
             compModels=compModels)
pf.show_completed_models(compModels)

##To oviod aliasing in funtions, send a copy of the list into the funtion
##funtionName = (listName[:]) slice the enitre list to send a copy
