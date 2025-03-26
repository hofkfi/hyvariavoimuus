import streamlit as st
import pandas as pd
import numpy as np

# Mock data for visualization
regions = ["Pohjois-Pohjanmaa", "Pirkanmaa", "Varsinais-Suomi", "Uusimaa", "Lapland"]
categories = ["Politiikka", "Portaali", "Laatu", "Vaikuttavuus"]
data = np.random.randint(50, 100, size=(5, 4))

# Create a DataFrame for the scores
df = pd.DataFrame(data, index=regions, columns=categories)

# Streamlit App Layout
st.title("Hyvinvointialueiden Open Data Maturity Mittaristo")
st.markdown("Tämä mittaristo visualisoi hyvinvointialueiden avoimen datan kypsyyden neljässä pääkategoriassa: Politiikka, Portaali, Laatu ja Vaikuttavuus.")

st.header("Mittariston Kokonaiskuva")
st.bar_chart(df)

st.header("Yksityiskohtainen Aluekohtainen Tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", regions)
region_data = df.loc[selected_region]

st.subheader(f"Hyvinvointialue: {selected_region}")
st.metric("Politiikka", region_data["Politiikka"])
st.metric("Portaali", region_data["Portaali"])
st.metric("Laatu", region_data["Laatu"])
st.metric("Vaikuttavuus", region_data["Vaikuttavuus"])

st.header("Indikaattorien Vertailu")
st.line_chart(df)

st.header("Yhteenveto ja Kehityssuositukset")
st.markdown("""
- **Politiikka:** Lisää koulutusta ja strategista ohjeistusta.
- **Portaali:** Varmista datan käytettävyys ja ajantasaisuus.
- **Laatu:** Paranna datan tarkkuutta ja anonymisointia.
- **Vaikuttavuus:** Seuraa datan käyttöastetta ja käyttäjäpalautetta.
""")
