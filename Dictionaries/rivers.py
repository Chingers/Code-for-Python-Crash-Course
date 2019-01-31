#6-5, Python Crash Course, Rivers

rivers = {
    "nile": "egypt",
    "hudson's bay": "canada",
    "st.lawrence": "canada",
    }

for river, country in rivers.items():
    print(river.title() + ": " + country.title())

print("\nRivers:")

for river in set(rivers.keys()):
    print(river)

print("\nCountries:")

for country in set(rivers.values()):
    print(country)
