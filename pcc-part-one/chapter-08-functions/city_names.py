def write_city_country(city_name, country_name):
    """Returns city-country pair, neatly formatted"""
    city_country = f"{city_name}, {country_name}"
    return city_country.title()


city_country_pair = write_city_country("brno", "czech republic")
print(city_country_pair)
city_country_pair = write_city_country("santiago", "chile")
print(city_country_pair)
city_country_pair = write_city_country("rome", "italy")
print(city_country_pair)
