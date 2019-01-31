#6-3, Python Crash Course, Glossary

glossary = {
    "variable": "a place where you can store data.",
    "for loop": "Data structure that loops an action a fixed amount of times.",
    "boolean expression": "An expression that evaluates to true or false.",
    "list": "A collection of items in a order.",
    "dictionary": "A collection of key-value pairs (does not have an order.)"
    }

#Loop iterates through every item in dictionary(key-value pair).
#Allows you to do different actions by assing variables word and definition
#to the keys and values.
for word, definition in sorted(glossary.items()):
    print("\n\n" + word + ":\n" + definition)
