from city_functions import get_city_country_pair


def test_city_country_name_pairs():
    """Test whether city-country pair working propperly."""
    city_country_pair = get_city_country_pair("santiago", "chile")
    assert city_country_pair == "Santiago, Chile."


def test_city_country_population_pairs():
    """Test if city-country-population trio working propperly."""
    city_country_population_pair = get_city_country_pair("santiago", "chile", "5000000")
    assert city_country_population_pair == "Santiago, Chile, Population - 5000000."
