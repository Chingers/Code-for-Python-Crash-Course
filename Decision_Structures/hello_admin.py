#5-8, Python Crash Course, Hello Admin

usernames = []#['mark', 'kyle' , 'bachels', 'monching', 'admin']

if usernames:
    for username in usernames:
        if username.lower() == 'admin':
            print("Greetings, Admin, would you like me to run an operation?")

        else:
            print("Hello " + username.title() + ", hope you're having a good day.")
            
else:
    print("Oh man, we really need some users.")
