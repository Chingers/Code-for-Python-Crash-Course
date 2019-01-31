#Returning a Simple Value

def get_formatted_name(firstName, lastName, middleName= ""):
    """Returns a full name, neatly formatted"""

    if middleName:
        fullName = firstName + " " + middleName + " " + lastName
    else:
        fullName = firstName + " " + lastName
        
    return fullName.title() #Returns the value to the line

musician = get_formatted_name(firstName= "jimi",lastName= "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee")
print(musician)

