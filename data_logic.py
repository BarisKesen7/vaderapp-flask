def is_valid_city(city_name):
    allowed_cities = (
        "Stockholm",
        "Göteborg",
        "Malmö",
        "Umeå",
        "Kiruna"
    )

    return city_name in allowed_cities

#Kontrollerar om den angivna staden finns med och returnerar True om staden tillåten, annars False.