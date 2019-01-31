#6-7, Python Crash Course, People

person0 = {
    "firstName": "bachel",
    "lastName": "copreros",
    "age": "14",
    "city": "brampton"
    }
person1 = {
    "firstName": "monching",
    "lastName": "copreros",
    "age": "16",
    "city": "brampton"
    }
person2 = {
    "firstName": "adrian",
    "lastName": "ayala",
    "age": "18",
    "city": "toronto"
    }

people = [person0, person1, person2]

for personInfo in people:
    print("First Name: " + personInfo["firstName"].title() +
      "\nLast Name: " + personInfo["lastName"].title() +
      "\nAge: " + personInfo["age"] +
      "\nCity: " + personInfo["city"] + "\n")
