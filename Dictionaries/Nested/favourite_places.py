#6-9, Python Crash Course, Favourite places

#Store people and their three favourite places

pplFavPlaces = {
    "monching": ["toronto", "silicon valley", "naples"],
    "rachel": ["brampton", "washroom", "couch"],
    "joy": ["rome", "ilo ilo", "jakarta"],
    }

for person, favPlaces in pplFavPlaces.items():
    print("\n" + person.title() + "'s, three favourite places are: ")
    for place in favPlaces:
        print("\t" + place.title())
    
