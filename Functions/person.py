#Returning more complicated values such as a dictionary

def build_person(firstName, lastName, age= ""):
    """Returns dictionary of information about a person"""
    person = {"first": firstName, "last": lastName}

    if age:
        person["age"] = age

    return person

musician = build_person("jimi", "hendrix", age= 27)
print(musician)
