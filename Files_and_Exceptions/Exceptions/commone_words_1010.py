#10-10, Python Crash Course, Common Words
#Counts the amount a certain word or phrase occurs in a file

#Functions
def count_occur(filename, phrase):
    """Count the occurences of the phrase given by user."""
    #filename = "Text_Files/" + filename
    try:
        with open(filename, "r") as objFile:
            contents = objFile.read()
            numOccured = contents.lower().count(phrase)
            
    except FileNotFoundError:
        print("Sorry, the file " + str(filename) + " was not found.\n")
    else:
        print("The phrase '" + str(phrase) + "' occured in the file " +
              str(filename) + " " + str(numOccured) + " times.\n")

#BODY
while True:
    print("Provide a file name and a phrase to see" +
          "\nhow many times the phrase occurs in the file!" +
          "\n(Enter 'q' to exit program).\n")
    
    fileNameGiven = input("File name: ")
    if (fileNameGiven == 'q'):
        break

    phraseGiven = input("Phrase: ")
    if (phraseGiven == 'q'):
        break

    count_occur(fileNameGiven, phraseGiven)

        
