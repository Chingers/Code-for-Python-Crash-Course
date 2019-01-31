#6-11, Python Crash Course, Cities

cities = {
    "naples": {
        "country": "italy",
        "population": 984000,
        "fact": "contains Castel Nuovo, a 13th-century castle"
        },
    "silicon valley": {
        "country": "america",
        "population": 3000000,
        "fact": "is home to largest number of millionares"
        },
    "toronto": {
        "country": "Canada",
        "population": 2809000,
        "fact": "contains the second largest building in the world (CN Tower)"
        },
    }

for city, cityInfo in cities.items():
    print("The city of " + city.title() +
          " is located in the country " + cityInfo["country"].title() +
          ", has a population of about " + str(cityInfo["population"]) +
          ", and " + cityInfo["fact"] + ".\n")
