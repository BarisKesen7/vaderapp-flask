import pytest
from app import app

@pytest.fixture
def klient():
    app.config["TESTING"] = True
    with app.test_client() as klient:
        yield klient

def test_huvud_sida(klient):
    svar = klient.get("/")

    assert svar.status_code == 200

    html_text = svar.get_data(as_text=True)
    assert "Välja en stad" in html_text