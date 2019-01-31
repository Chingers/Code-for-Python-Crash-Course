#Project 3-5, Python Crash Course, Changing Guest List

guests = ['Jesus', 'darwhin', 'tyson']
missing = guests[2]
print('\nHello ' + guests[0].title() + ', ' + guests[1].title() + ', and ' + guests[2].title() + ', you are all invited to my dinner.')
print('Sorry, but ' + missing + ' cannot make the dinner.')

guests[2] = 'hawking'
print('Hello ' + guests[0].title() + ', ' + guests[1].title() + ', and ' + guests[2].title() + ', you are all invited to my dinner./n')

#Project 3-6, Python Crash Course, More Guests

print('\nAttention, it looks like i have found a bigger dinner table.')
guests.insert(0, 'Einstein')
guests.insert(1, 'Samberg')
guests.append('Buddha')

print('Hello ' + guests[0].title() + ', ' + guests[1].title()  + ', ' + guests[2].title() + ', ' + guests[3].title() + ', ' + guests[4].title() + ', and ' + guests[5].title() + ', you are all invited to my dinner.\n')

#Project 3-7, Python Crash Course, Shrinking Guest lists

print('Oh no, there has been a complication and now only two people can come to my dinner.')

cant = guests.pop()
print('I am truly sorry, but ' + cant + ' is no longer invited to my dinner')
cant = guests.pop()
print('I am truly sorry, but ' + cant + ' is no longer invited to my dinner')
cant = guests.pop()
print('I am truly sorry, but ' + cant + ' is no longer invited to my dinner')
cant = guests.pop()
print('I am truly sorry, but ' + cant + ' is no longer invited to my dinner')

print('Hello ' + guests[0].title() + ' and ' + guests[1].title() + ', you both are still invited\n')

del guests[1]
del guests[0]

print(guests)
