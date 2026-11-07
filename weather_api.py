import requests

class VaderApiError(Exception):
    pass

#egen felhantering när något går fel med API:et

def hamta_vader(latitud, longitud):
#hämtar data från open-meteo för angivna koordinater
    api_url = "https://api.open-meteo.com/v1/forecast"

    egenskaper = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 3
    }

    try:
        svar = requests.get(api_url, params= egenskaper, timeout=5)
        svar.raise_for_status()
        return svar.json()

    except requests.RequestException:
        raise VaderApiError("API:et svarade inte eller ett fel uppstod.")

#här fångas fel och kastar vårt eget fel som testet letar efter.