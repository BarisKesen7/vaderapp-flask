from flask import Flask, render_template, request

from data_logic import is_valid_city
from diagram import skapa_diagram
from weather_api import VaderApiError, hamta_vader

app = Flask(__name__)
# En dictionary som kopplar varje godkänd stad till dess koordinater (latitud, longitud)
stad_koordinater = {
    "Stockholm": (59.33, 18.06),
    "Göteborg": (57.71, 11.97),
    "Malmö": (55.60, 13.00),
    "Umeå": (63.83, 20.26),
    "Kiruna": (67.85, 20.22),
}

# här är det huvudsidan av programmet


@app.route("/", methods=["GET", "POST"])
def huvud_sida():
    # Sätter startvärden innan användaren har gjort en sökning
    vader_data = None
    felmeddelande = None
    vald_stad = None
    diagram_html = None
    status_kod = 200

    if request.method == "POST":
        # Hämtar den stad som användaren valde i formuläret
        vald_stad = request.form.get("stad")

        if not is_valid_city(vald_stad):
            felmeddelande = "Ogiltigt stad vald."
            status_kod = 400  # 400 Bad Request
        else:
            latitud, longitud = stad_koordinater[vald_stad]
            try:
                vader_data = hamta_vader(latitud, longitud)
                diagram_html = skapa_diagram(vader_data["daily"])
            except VaderApiError as e:
                felmeddelande = str(e)
                status_kod = 500
    # Skickar all data till index.html för att visas på webbsidan, inklusive rätt statuskod
    return render_template(
        "index.html",
        data=vader_data,
        fel=felmeddelande,
        stad=vald_stad,
        diagram=diagram_html,
    ), status_kod


if __name__ == "__main__":
    app.run(debug=True)

# gör att servern laddar om automatiskt när man sparar koden
