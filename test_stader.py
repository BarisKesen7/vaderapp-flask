import pytest
from data_logic import is_valid_city

@pytest.mark.parametrize("city, expected", [
    ("Stockholm", True),
    ("Kiruna", True),
    ("Istanbul", False),
    ("stockholm", False)
])

def test_is_valid_city(city, expected):
    assert is_valid_city(city) == expected
    
#testar att funktionerna enbart godkänner de fem bestämda städer