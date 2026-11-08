# Svenska Väderappen 🌤️

En webbapplikation byggd med Python och Flask som hämtar och visar aktuellt väder samt en interaktiv temperaturprognos för utvalda svenska städer.

## Teknologier som används
* **Backend:** Python, Flask
* **Data & Grafer:** Pandas, Plotly
* **Frontend:** HTML, Jinja2, Bootstrap
* **Testning:** Pytest, pytest-mock

## 🛠️ Installation

1. Öppna projektmappen i VS Code.
2. Skapa en virtuell miljö genom att köra detta i terminalen:
   ```bash
   python -m venv venv
   ```
3. Aktivera den virtuella miljön:
   * **Windows:** `venv\Scripts\activate`
   * **Mac/Linux:** `source venv/bin/activate`
4. Installera alla nödvändiga paket:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Hur du kör appen

När den virtuella miljön är aktiverad och paketen är installerade, starta servern med:
```bash
python app.py
```
Öppna sedan en webbläsare och gå till: `http://127.0.0.1:5000/`

## 🧪 Hur du kör testerna

Kör alla tester genom att skriva följande i terminalen:
```bash
pytest
```

## 📝 Svar på frågor

1. Jag mockar API-anropen för att testerna ska gå snabbt och fungera utan internet. Om jag inte gjorde det skulle testerna krascha om API:et ligger nere, och appen skulle riskera att bli blockerad för att ha skickat för många anrop under testningen.

2. `timeout` förhindrar att programmet fastnar för evigt om servern är långsam. `raise_for_status()` kollar att svaret är okej (status 200) och skapar automatiskt ett felmeddelande om något går snett, vilket jag sedan fångar upp.

3. Mallarv gör att man slipper skriva samma HTML-kod flera gånger. I min app ärver `index.html` hela grunddesignen och Bootstrap-länken från `base.html` med hjälp av koden `{% extends "base.html" %}`.

4. En fixture förbereder en testmiljö så att man slipper upprepa kod i varje test. Jag använder en fixture som heter `klient()` i `test_app.py` för att sätta upp Flasks testklient. Det låter mig testa webbsidan utan att starta själva servern.