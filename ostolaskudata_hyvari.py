import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sivuasetukset ilman wide-tilaa
st.set_page_config(page_title="Ostolaskudata 2025")

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
    "Vuosi": [
        2023, 2023, 2023, 2023,
        2023, 2024, 2020, 2023,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None
    ],
    "Muoto": [
        "Dataset", "Excel (ladattava)", "Dataset (osana aineistoa)",
        "Dataset (osana aineistoa)", "Excel (ladattava)",
        "Power BI -raportti", "Dataset", "Excel (ladattava)",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ],
    "Lähde": [
        "Avoindata.fi", "paijatha.fi", "Tutkihankintoja.fi",
        "Tutkihankintoja.fi", "Eloisan verkkosivut",
        "Keusote / Tietojohtaja", "Avoindata.fi", "Avoindata.fi",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ]
}
df = pd.DataFrame(data)

# Aloitus
st.title("📊 Hyvinvointialueiden Ostolaskudatan Julkaisutilanne – 2025")

st.markdown("""
Tämä sovellus esittää Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteen maaliskuussa 2025. 
Voit tarkastella kokonaistilannetta tai valita yksittäisen alueen nähdäksesi tarkemmat tiedot.
""")

# Kokonaiskuva
st.header("Kokonaiskuva Julkaisutilanteesta")
st.bar_chart(df["Julkaistu"].value_counts())

# Valinta ja tarkastelu
st.header("Yksittäisen Alueen Tiedot")
alue = st.selectbox("Valitse hyvinvointialue", df["Hyvinvointialue / Erityisyksikkö"])
rivi = df[df["Hyvinvointialue / Erity
