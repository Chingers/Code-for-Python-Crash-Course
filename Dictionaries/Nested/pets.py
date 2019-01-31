#6-8, Python Crash Course, Pets

jacko = {
    "name": "Jacko",
    "kind": "dog",
    "owner": "monit",
    }
merlin = {
    "name": "merlin",
    "kind": "bird",
    "owner": "raina",
    }
pogi = {
    "name": "pogi",
    "kind": "dog",
    "owner": "josh",
    }
kitkat = {
    "name": "kit kat",
    "kind": "cat",
    "owner": "raina",
    }

pets = [jacko, merlin, pogi, kitkat]

for pet in pets:
    print(pet["owner"].title() + "'s, pet " +
          pet["name"].title() + " is a " +
          pet["kind"] + ".\n")
