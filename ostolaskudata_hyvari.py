import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Sivuasetukset
st.set_page_config(page_title="Ostolaskudata 2025", layout="wide")

# Sidebar: ohjeet ja linkit
st.sidebar.title("📚 Ohjeet ja linkit")
st.sidebar.markdown("""
**🔗 Kuntaliiton ohjeistus:**  
[Kuntaliiton suositukset avoimen datan julkaisemiseen](https://www.kuntaliitto.fi/tietoa-kunnista/paattajalle/avoin-data)

**🌐 Avoindata.fi Julkaisijan opas:**  
[Avoindata.fi - Julkaisijan ohjeet](https://www.avoindata.fi/fi/info/publisher-guide)

**🛡️ Tietosuoja ja anonymisointi:**  
[VM:n arviomuistio 2024](https://www.lausuntopalvelu.fi/)

**🧰 Työkalut:**  
- [OpenRefine](https://openrefine.org/) – tietojen siivoamiseen ja rakenteistamiseen  
- [Open Data Editor](https://github.com/OKFIFinland/Open-Data-Editor) – no-code-työkalu julkaistun datan katseluun, tarkistukseen ja korjaukseen ilman ohjelmointia  
- [DCAT-AP Validator](https://www.dcat-ap-validator.eu/) – tekninen validointityökalu metatiedon yhteentoimivuuden tarkistamiseen (DCAT-AP-standardit)
""")

# Data (ilman HUSia ja Ahvenanmaata)
data = [
    ["Varsinais-Suomi", "Kyllä", "Avoindata.fi", "20.2.2024", "https://www.opendata.fi/data/fi/dataset/varha-ostolaskut"],
    ["Päijät-Häme", "Kyllä", "Alueen omat sivut", "2023", ""],
    ["Pirkanmaa", "Kyllä", "Tutkihankintoja.fi", "2023", "https://www.tutkihankintoja.fi/fi/search?orgs=pirkanmaa"],
    ["Pohjois-Pohjanmaa", "Kyllä", "Tutkihankintoja.fi", "2023", "https://www.tutkihankintoja.fi/fi/search?orgs=ppo"],
    ["Etelä-Savo (Eloisa)", "Kyllä", "Eloisa.fi", "2023", "https://etelasavonha.fi/ostolaskut"],
    ["Keski-Uusimaa", "Kyllä", "Power BI", "2024", "https://www.keusote.fi/ostolaskut"],
    ["Pohjois-Savo", "Kyllä", "Avoindata.fi", "2023", "https://www.opendata.fi/data/fi/dataset/pohjois-savo-ostolaskut"],
    ["Kanta-Häme", "Ei", "-", "-", ""],
    ["Kymenlaakso", "Ei", "-", "-", ""],
    ["Satakunta", "Ei", "-", "-", ""],
    ["Pohjois-Karjala", "Ei", "-", "-", ""],
    ["Keski-Pohjanmaa", "Ei", "-", "-", ""],
    ["Lappi", "Ei", "-", "-", ""],
    ["Kainuu", "Ei", "-", "-", ""],
    ["Etelä-Karjala", "Ei", "-", "-", ""],
    ["Etelä-Pohjanmaa", "Ei", "-", "-", ""],
    ["Keski-Suomi", "Ei", "-", "-", ""],
    ["Itä-Savo", "Ei", "-", "-", ""],
    ["Länsi-Pohja", "Ei", "-", "-", ""],
    ["Vaasa", "Ei", "-", "-", ""],
    ["Itä-Uusimaa", "Ei", "-", "-", ""],
    ["Länsi-Uusimaa", "Ei", "-", "-", ""],
    ["Vantaa ja Kerava", "Ei", "-", "-", ""]
]

np.random.seed(42)
latitude = np.random.uniform(60.0, 66.0, len(data))
longitude = np.random.uniform(21.0, 28.0, len(data))

# DataFrame
columns = ["Hyvinvointialue", "Julkaistu", "Julkaisualusta", "Päivitetty", "Lähde"]
df = pd.DataFrame(data, columns=columns)
df["Latitude"] = latitude
df["Longitude"] = longitude
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
    initial_view_state=pdk.ViewState(latitude=63.0, longitude=25.0, zoom=4.2),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position='[Longitude, Latitude]',
            get_fill_color="Color",
            get_radius=30000,
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
