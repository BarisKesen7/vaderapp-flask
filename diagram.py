import pandas as pd
import plotly.express as px


def skapa_diagram(daglig_data):
    # Skapar en Pandas DataFrame med datum och temperaturer
    df = pd.DataFrame(
        {
            "Datum": daglig_data["time"],
            "Max Temperatur (°C)": daglig_data["temperature_2m_max"],
            "Min Temperatur (°C)": daglig_data["temperature_2m_min"],
        }
    )
    # Ett interaktivt linjediagram där X-axeln är datum och Y-axeln visar max- och mintemperatur
    linje_diagram = px.line(
        df,
        x="Datum",
        y=["Max Temperatur (°C)", "Min Temperatur (°C)"],
        title="Temperaturprognos",
        markers=True,
        labels={"value": "Temperatur", "variable": "Mätning"},
    )
    # Gör diagrammets bakgrund helt genomskinlig
    linje_diagram.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin={"l": 20, "r": 20, "t": 40, "b": 20},
    )
    # Konverterar Plotly-diagrammet till ren HTML-kod så att det kan visas direkt i index.html
    return linje_diagram.to_html(full_html=False, include_plotlyjs="cdn")
