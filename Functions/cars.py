#8-14, Python Crash Course, Cars

#Functions
def make_car(manufacturer, model, **carInfo):
    """Builds a dictionary containing everything we know about a car"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in carInfo.items():
        car[key] = value
    return car

car = make_car('dodge', 'caravan', seats= "7", hp= "5500")
print(car)
