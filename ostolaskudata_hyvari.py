import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Sivuasetukset
st.set_page_config(page_title="Ostolaskudata 2025", layout="wide")

# Sidebar: ohjeet ja linkit
with st.sidebar:
    st.title("📚 Ohjeet ja linkit")
    st.markdown("""
    **🔗 Kuntaliiton ohjeistus:**  
    [Kuntaliiton suositukset avoimen datan julkaisemiseen](https://www.kuntaliitto.fi/tietoa-kunnista/paattajalle/avoin-data)

    **🌐 Avoindata.fi Julkaisijan opas:**  
    [Avoindata.fi - Julkaisijan ohjeet](https://www.avoindata.fi/fi/kayttoohjeet)

    **🧰 Työkalut:**  
    - [OpenRefine](https://openrefine.org/) – tietojen siivoamiseen ja rakenteistamiseen  
    - [Open Data Editor](https://github.com/OKFIFinland/Open-Data-Editor) – no-code-työkalu julkaistun datan katseluun, tarkistukseen ja korjaukseen ilman ohjelmointia  
    - [DCAT-AP Validator](https://www.dcat-ap-validator.eu/) – tekninen validointityökalu metatiedon yhteentoimivuuden tarkistamiseen (DCAT-AP-standardit)
    """)

    st.markdown("""
    **ℹ️ Huomautus:** Tässä visualisoinnissa keskitytään Suomen 21 hyvinvointialueeseen, jotka perustettiin vuonna 2021 sote-uudistuksen yhteydessä. 
    Ahvenanmaa ja Helsingin kaupunki (joilla on oma järjestämisvastuu) sekä HUS (joka on erityisyksikkö) on rajattu ulkopuolelle.
    Vain viralliset hyvinvointialueet on sisällytetty karttaan ja vertailuun.
    """)

# Data – tarkennettu 21 hyvinvointialueeseen
# Hyvinkää poistettu, Kainuu palautettu mukaan
# Koordinaatit säädetty

data = [
    ["Varsinais-Suomi", "Kyllä", "Avoindata.fi", "20.2.2024", "https://www.opendata.fi/data/fi/dataset/varha-ostolaskut", 60.45, 22.26],
    ["Päijät-Häme", "Kyllä", "Alueen omat sivut", "2023", "", 60.98, 25.66],
    ["Pirkanmaa", "Kyllä", "Tutkihankintoja.fi", "2023", "https://www.tutkihankintoja.fi/fi/search?orgs=pirkanmaa", 61.50, 23.77],
    ["Pohjois-Pohjanmaa", "Kyllä", "Tutkihankintoja.fi", "2023", "https://www.tutkihankintoja.fi/fi/search?orgs=ppo", 65.01, 25.47],
    ["Etelä-Savo", "Kyllä", "Eloisa.fi", "2023", "https://etelasavonha.fi/ostolaskut", 61.68, 27.27],
    ["Keski-Uusimaa", "Kyllä", "Power BI", "2024", "https://www.keusote.fi/ostolaskut", 60.41, 25.08],
    ["Pohjois-Savo", "Kyllä", "Avoindata.fi", "2023", "https://www.opendata.fi/data/fi/dataset/pohjois-savo-ostolaskut", 62.89, 27.68],
    ["Kanta-Häme", "Ei", "-", "-", "", 60.99, 24.46],
    ["Kymenlaakso", "Ei", "-", "-", "", 60.57, 26.86],
    ["Satakunta", "Ei", "-", "-", "", 61.49, 21.80],
    ["Pohjois-Karjala", "Ei", "-", "-", "", 62.60, 29.76],
    ["Keski-Pohjanmaa", "Ei", "-", "-", "", 63.73, 23.12],
    ["Lappi", "Ei", "-", "-", "", 67.73, 24.65],
    ["Kainuu", "Ei", "-", "-", "", 64.13, 27.67],
    ["Etelä-Karjala", "Ei", "-", "-", "", 61.06, 28.19],
    ["Etelä-Pohjanmaa", "Ei", "-", "-", "", 62.79, 22.84],
    ["Keski-Suomi", "Ei", "-", "-", "", 62.24, 25.75],
    ["Itä-Savo", "Ei", "-", "-", "", 62.02, 28.29],
    ["Itä-Uusimaa", "Ei", "-", "-", "", 60.40, 25.22],
    ["Länsi-Uusimaa", "Ei", "-", "-", "", 60.13, 24.38],
    ["Vantaa ja Kerava", "Ei", "-", "-", "", 60.31, 25.02]
]

columns = ["Hyvinvointialue", "Julkaistu", "Julkaisualusta", "Päivitetty", "Lähde", "Latitude", "Longitude"]
df = pd.DataFrame(data, columns=columns)
df["Color"] = df["Julkaistu"].apply(lambda x: [0, 200, 0] if x == "Kyllä" else [200, 0, 0])

# CSV-lataus
csv = df.to_csv(index=False).encode("utf-8")
st.sidebar.download_button("📥 Lataa CSV", csv, "ostolaskudata_2025.csv", "text/csv")

# Titteli
st.title("📊 Hyvinvointialueiden Ostolaskudatan Julkaisutilanne – 2025")
st.markdown("Tämä sovellus esittää Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteen maaliskuussa 2025.")

# Kartta
st.header("🗺️ Karttanäkymä: Julkaisutilanne")
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=63.0, longitude=25.0, zoom=4.3),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position='[Longitude, Latitude]',
            get_fill_color="Color",
            get_radius=25000,
            pickable=True
        )
    ],
    tooltip={"text": "{Hyvinvointialue}\nJulkaistu: {Julkaistu}"}
))

# Julkaisujen määrä
st.header("📈 Kokonaiskuva Julkaisutilanteesta")
st.bar_chart(df["Julkaistu"].value_counts())

# Valitse alue
st.header("🔍 Yksittäisen Alueen Tiedot")
alue = st.selectbox("Valitse hyvinvointialue", df["Hyvinvointialue"])
rivi = df[df["Hyvinvointialue"] == alue].iloc[0]
st.markdown(f"""
**Hyvinvointialue:** {alue}  
**Julkaistu:** {rivi['Julkaistu']}  
**Julkaisualusta:** {rivi['Julkaisualusta']}  
**Päivitetty:** {rivi['Päivitetty']}  
**Lähde:** {rivi['Lähde']}  
""")

# Yhteenveto
st.header("🧭 Yhteenveto ja Kehitysehdotuksia")
st.markdown("""
- 💡 Tarvetta harmonisoida julkaisutavat ja -formaatit.  
- 🌐 Avoindata.fi tai vastaava yhteinen portaali parantaisi saatavuutta.  
- 🔍 Tiedon löydettävyyttä ja käytettävyyttä voi parantaa metatiedon laadulla.  
""")
