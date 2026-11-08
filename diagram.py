import pandas as pd 
import plotly.express as px

def skapa_diagram(daglig_data):
    df = pd.DataFrame({
        "Datum": daglig_data["time"],
        "Max Temperatur (°C)": daglig_data["temperature_2m_max"],
        "Min Temperatur (°C)": daglig_data["temperature_2m_min"]
    })

    linje_diagram = px.line(
        df,
        x="Datum",
        y=["Max Temperatur (°C)", "Min Temperatur (°C)"],
        title="Temperaturprognos",
        markers=True,
        labels={"value": "Temperatur", "variable": "Mätning"}
    )

    linje_diagram.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return linje_diagram.to_html(full_html=False, include_plotlyjs='cdn')