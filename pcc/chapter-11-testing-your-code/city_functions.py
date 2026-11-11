def get_city_country_pair(city, country, population=""):
    """Returns a city-country pair, neatly formatted."""
    if population:
        city_country_pair = f"{city}, {country}, population - {population}."
    else:
        city_country_pair = f"{city}, {country}."
    return city_country_pair.title()
