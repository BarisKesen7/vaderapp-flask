import pytest
import requests

from weather_api import VaderApiError, hamta_vader


def test_hamta_vader(mocker):
    mocker.patch("requests.get", side_effect=requests.Timeout)

    with pytest.raises(VaderApiError) as fel_info:
        hamta_vader(59.33, 18.06)

    assert "svarade inte" in str(fel_info.value).lower()


# testar Stockholms koordinater med rätt latitud och lonitud värden, om fel kastar direkt ett Timeout-fel
