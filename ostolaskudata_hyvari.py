import streamlit as st
import pandas as pd

# Kovakoodattu data taulukosta
data = {
    "Hyvinvointialue / Erityisyksikkö": [
        "Varsinais-Suomi", "Päijät-Häme", "Pirkanmaa", "Pohjois-Pohjanmaa", 
        "Etelä-Savo (Eloisa)", "Keski-Uusimaa", "HUS", "Pohjois-Savo",
        "Kanta-Häme", "Kymenlaakso", "Satakunta", "Pohjois-Karjala",
        "Keski-Pohjanmaa", "Lappi", "Kainuu", "Etelä-Karjala",
        "Etelä-Pohjanmaa", "Keski-Suomi", "Ahvenanmaa", "Itä-Savo",
        "Länsi-Pohja", "Vaasa"
    ],
    "Julkaistu?": [
        "Kyllä", "Kyllä", "Kyllä", "Kyllä", 
        "Kyllä", "Kyllä/Tulossa", "Kyllä", "Kyllä",
        "Ei julkaistu", "Ei julkaistu", "Ei julkaistu", "Ei julkaistu",
        "Ei julkaistu", "Ei julkaistu", "Ei julkaistu", "Ei julkaistu",
        "Ei julkaistu", "Ei julkaistu", "Ei julkaistu", "Ei julkaistu",
        "Ei julkaistu", "Ei julkaistu"
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
        "Dataset", "Excel-tiedosto (ladattava)", "Dataset (osana isoa aineistoa)", 
        "Dataset (osana isoa aineistoa)", "Excel-tiedosto (ladattava)", 
        "Raportointi (Power BI)", "Dataset", "Excel-tiedosto (ladattava)",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ],
    "Lähde": [
        "Avoindata.fi", "paijatha.fi", "Tutkihankintoja.fi (avoindata.fi aineisto)", 
        "Tutkihankintoja.fi (avoindata.fi aineisto)", "Eloisan verkkosivut", 
        "Päättäjäskirja (Keusote) / Tietojohtajan sähköposti", 
        "Avoindata.fi (HUS ostolaskut)", "Avoindata.fi",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ],
    "Lisätieto": [
        "Erillinen datasetti Avoindata.fi:ssä. Varha avasi ostolaskudatan ensimmäisenä hyvinvointialueena.",
        "Data ladattavissa hyvinvointialueen sivuilta (ostolaskudata 2023 XLSX).",
        "2025 aineistossa ei vielä mukana, vain valtion laskut. Päivitystiheys epäselvä. Puolivuosittain?",
        "2025 aineistossa ei vielä mukana, vain valtion laskut. Päivitystiheys epäselvä.",
        "Julkaistaan jatkossa kerran vuodessa.",
        "Päivittyy 1x/kk Power BI -raporttina, ei vielä julkaistu verkkosivuilla.",
        "HUS toimii poikkeuksellisena julkisuusvelvollisuuden yhteisönä Uudenmaan alueella. Julkaisee ostolaskut 4x/vuosi.",
        "Data julkaistu tilinpäätöksen valmistuttua 2024.",
        "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa",
        "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa",
        "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa", "Ei lisätietoa",
        "Ei lisätietoa", "Ei lisätietoa"
    ]
}

# Luodaan DataFrame
df = pd.DataFrame(data)

# Streamlit-sovellus
st.title("Hyvinvointialueiden Ostolaskudatan Julkaisutilanne 2025")
st.markdown("Päivitetty lista Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteesta maaliskuussa 2025.")

# Suodatus hyvinvointialueen mukaan
selected_region = st.selectbox("Valitse hyvinvointialue", ["Kaikki"] + list(df["Hyvinvointialue / Erityisyksikkö"]))
if selected_region != "Kaikki":
    filtered_df = df[df["Hyvinvointialue / Erityisyksikkö"] == selected_region]
else:
    filtered_df = df

# Näytetään taulukko
st.dataframe(filtered_df)

# Yhteenveto julkaisutilanteesta
published_count = len(df[df["Julkaistu?"] == "Kyllä"]) + len(df[df["Julkaistu?"] == "Kyllä/Tulossa"])
total_count = len(df)
st.markdown(f"**Julkaistuja tai tulossa olevia alueita:** {published_count} / {total_count}")
st.bar_chart(df["Julkaistu?"].value_counts())

# Kehitysehdotukset
st.header("Yhteenveto ja Kehitysehdotukset")
st.markdown("""
- **Tietojen päivittäminen:** Varmista, että kaikki julkaisutiedot ovat ajan tasalla.
- **Tietolähteiden yhtenäistäminen:** Käytä keskitettyä portaalia (esim. Avoindata.fi) datan löydettävyyden parantamiseksi.
- **Päivitystiheys:** Selkeytä päivitystiheys kaikille alueille.
- **Tiedon laatu:** Varmista, että datamuodot ja tiedostotyypit ovat yhtenäisiä.
""")
