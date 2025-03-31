import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

# Sivuasetukset
st.set_page_config(page_title="Ostolaskudata 2025", layout="centered")

# Datan luonti
data = {
    "Hyvinvointialue / Erityisyksikkö": [
        "Varsinais-Suomi", "Päijät-Häme", "Pirkanmaa", "Pohjois-Pohjanmaa",
        "Etelä-Savo (Eloisa)", "Keski-Uusimaa", "HUS", "Pohjois-Savo",
        "Kanta-Häme", "Kymenlaakso", "Satakunta", "Pohjois-Karjala",
        "Keski-Pohjanmaa", "Lappi", "Kainuu", "Etelä-Karjala",
        "Etelä-Pohjanmaa", "Keski-Suomi", "Ahvenanmaa", "Itä-Savo",
        "Länsi-Pohja", "Vaasa"
    ],
    "Julkaistu": [
        "Kyllä", "Kyllä", "Kyllä", "Kyllä",
        "Kyllä", "Kyllä", "Kyllä", "Kyllä",
        "Ei", "Ei", "Ei", "Ei",
        "Ei", "Ei", "Ei", "Ei",
        "Ei", "Ei", "Ei", "Ei",
        "Ei", "Ei"
    ],
    "Latitude": np.random.uniform(60.0, 66.0, 22),
    "Longitude": np.random.uniform(21.0, 28.0, 22)
}
df = pd.DataFrame(data)

# Sovelluksen alku
st.title("📊 Hyvinvointialueiden Ostolaskudatan Julkaisutilanne – 2025")
st.markdown("Tämä sovellus esittää Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteen maaliskuussa 2025.")

# Kartta
st.header("🗺️ Karttanäkymä: Julkaisutilanne")
df["Color"] = df["Julkaistu"].apply(lambda x: [0, 200, 0] if x == "Kyllä" else [200, 0, 0])
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=63.0,
        longitude=25.0,
        zoom=4.2,
        pitch=0,
    ),
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
    tooltip={"text": "{Hyvinvointialue / Erityisyksikkö}\nJulkaistu: {Julkaistu}"}
))

# Kokonaiskuva
st.header("Kokonaiskuva Julkaisutilanteesta")
st.bar_chart(df["Julkaistu"].value_counts())

# Yksittäinen alue
st.header("Yksittäisen Alueen Tiedot")
alue = st.selectbox("Valitse hyvinvointialue", df["Hyvinvointialue / Erityisyksikkö"])
rivi = df[df["Hyvinvointialue / Erityisyksikkö"] == alue].iloc[0]

st.markdown(f"""
**Hyvinvointialue:** {alue}  
**Julkaistu:** {rivi["Julkaistu"]}  
""")

# Yhteenveto
st.header("🧭 Yhteenveto ja Kehitysehdotuksia")
st.markdown("""
- 💡 Tarvetta harmonisoida julkaisutavat ja -formaatit.
- 🌐 Avoindata.fi tai vastaava yhteinen portaali parantaisi saatavuutta.
- 🔍 Tiedon löydettävyyttä ja käytettävyyttä voi parantaa metatiedon laadulla.
""")
