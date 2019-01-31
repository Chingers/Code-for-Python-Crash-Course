#Nesting a Dictionary into a dictionary

#store users and users information in dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
        },
    "mcurrie": {
        "first": "marie",
        "last": "currie",
        "location": "paris",
        },
    }

#Summarize the users info and usename
for user, userInfo in users.items():
    print("Username: " + user)
    fullName = userInfo["first"] + " " + userInfo["last"]
    location = "Location: " + userInfo["location"]

    print("Full name: " + fullName.title() +
          "\nLocation: " + location.title() + "\n")
