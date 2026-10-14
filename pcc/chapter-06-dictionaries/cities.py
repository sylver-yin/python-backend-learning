cities = {
    "london": {
        "country": "great britan",
        "population": "Enough",
        "fact": "you can drink tea here",
    },
    "dnipro": {
        "country": "ukraine",
        "population": "more than 2",
        "fact": "cool river",
    },
    "brno": {
        "country": "czech republic",
        "population": "yes",
        "fact": "cool IT hub",
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tApproximate population: {info['population']}")
    print(f"\tFact: {info['fact']}")
