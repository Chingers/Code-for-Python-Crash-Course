#86, Python Crash Course, City Names

def city_country(city, country):
    """Displays formatted message of city and country"""
    message = city.title() + ", " + country.title()

    return message

phrase = city_country("toronto", "canada")
print(phrase)
