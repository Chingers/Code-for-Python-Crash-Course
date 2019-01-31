#Handling FileNotFoundError Exception

#Functions
def count_words(filename):
    """Counts approximate amount of words in a file"""
    try:
        with open(filename, encoding="utf-8") as objFile:
            contents = objFile.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " could not be found."
        print(msg)
    else:
        words = contents.split()
        length = len(words)
        print("The file " + filename + " has about " + str(length) + " words.")

files = ["alice.txt",]

for file in files:
    count_words(file)
