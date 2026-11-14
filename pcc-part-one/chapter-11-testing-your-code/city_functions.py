def get_city_country_pair(city, country, population=""):
    """Return a city-country pair, neatly formatted."""
    if population:
        city_country_pair = f"{city}, {country}, population - {int(population)}."
    else:
        city_country_pair = f"{city}, {country}."
    return city_country_pair.title()
