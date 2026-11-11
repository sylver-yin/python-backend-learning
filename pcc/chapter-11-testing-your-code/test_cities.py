from city_functions import get_city_country_pair


def test_city_country_name_pairs():
    """Test whether city-country pair working propperly."""
    city_country_pair = get_city_country_pair("santiago", "chile")
    assert city_country_pair == "Santiago, Chile"
