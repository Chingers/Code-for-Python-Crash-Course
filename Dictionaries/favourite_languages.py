#6-6, Python Crash Courses, Polling

#Dictionary that holds name of person (key) anf favourite language (value)
favLanguages =  {
    "george": "Python",
    "mike": "Java",
    "rachel": "Scratch",
    "monching": "Python",
    "ekagra": "C++",
    }

#List that holds names of people that must take the poll
pollTakers = ["george", "stacy", "ekagra", "monching", "chris", "jim"]

#For loop that iterates through all items in pollTakers list
for pollTaker in pollTakers:
    #If name in the pollTakers list is  not in the favLanguages dictionary...
    if pollTaker.lower() not in favLanguages.keys():
        print(pollTaker.title() + ", please take the favourite language poll.")
    #If name in pollTakers list is in the favLanguages dictoinary...
    elif pollTaker.lower() in favLanguages.keys():
        print(pollTaker.title() + ", thank you for taking the poll!")
