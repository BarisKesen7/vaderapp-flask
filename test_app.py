import pytest

from app import app


# Skapar en fixture för att kunna testa webbsidan utan att behöva starta servern
@pytest.fixture
def klient():
    app.config["TESTING"] = True
    with app.test_client() as klient:
        yield klient


# Testar att startsidan laddar korrekt (statuskod 200) och innehåller förväntad text
def test_huvud_sida(klient):
    svar = klient.get("/")

    assert svar.status_code == 200

    html_text = svar.get_data(as_text=True)
    assert "Välja en stad" in html_text


# Gör om sidans innehåll till vanlig text för att enklare verifiera HTML-koden
