import streamlit as st
import pandas as pd
import numpy as np

# Hyvinvointialueet ja mittarit
regions = ["Pohjois-Pohjanmaa", "Pirkanmaa", "Varsinais-Suomi", "Uusimaa", "Lapland"]
categories = ["Politiikka", "Portaali", "Laatu", "Vaikuttavuus"]
indicators = {
    "Politiikka": ["Avoimen datan strategia", "Lainsäädännön noudattaminen", "Koulutus ja tuki"],
    "Portaali": ["Portaalin käytettävyys", "Teknologinen infrastruktuuri", "Avoimuuden indikaattorit"],
    "Laatu": ["Datan täydellisyys", "Datan tarkkuus", "Anonymisointi"],
    "Vaikuttavuus": ["Datan käyttöaste", "Käyttäjäpalaute", "Talousvaikutukset"]
}

# Kokonaiskuvan data
data = np.random.randint(50, 100, size=(5, 4))
df_summary = pd.DataFrame(data, index=regions, columns=categories)

# Indikaattorikohtainen data
data_detailed = {}
for category, questions in indicators.items():
    for question in questions:
        data_detailed[question] = np.random.randint(50, 100, size=len(regions))
df_detailed = pd.DataFrame(data_detailed, index=regions)

# Streamlit App Layout
st.title("Hyvinvointialueiden Avoimuus -Mittaristo")
st.markdown("""
Tämä mittaristo perustuu Open Data Maturity Index -mittaristoon ja Open Knowledge Finlandin tekemään tutkimukseen, jonka tavoitteena on auttaa hyvinvointialueita avoimuuden mittaroinnissa.
Tämä mittaristo visualisoi hyvinvointialueiden avoimen datan kypsyyden neljässä pääkategoriassa: 
- **Politiikka**
- **Portaali**
- **Laatu**
- **Vaikuttavuus**

Voit valita tietyn alueen ja indikaattorin tarkasteluun sekä verrata indikaattorin arvoja eri alueiden kesken.
""")
# Mittariston kokonaiskuva
st.header("Mittariston Kokonaiskuva")
st.bar_chart(df_summary)

# Aluekohtainen tarkastelu
st.header("Yksityiskohtainen Aluekohtainen Tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", regions)
region_data = df_summary.loc[selected_region]

st.subheader(f"Hyvinvointialue: {selected_region}")
st.metric("Politiikka", region_data["Politiikka"])
st.metric("Portaali", region_data["Portaali"])
st.metric("Laatu", region_data["Laatu"])
st.metric("Vaikuttavuus", region_data["Vaikuttavuus"])

# Indikaattorin vertailu eri alueiden välillä
st.header("Indikaattorin Vertailu")
st.markdown("Valitse kategoria ja sen sisällä oleva indikaattori nähdäksesi alueiden vertailun.")
selected_category = st.selectbox("Valitse kategoria", list(indicators.keys()))
selected_indicator = st.selectbox("Valitse indikaattori", indicators[selected_category])

st.subheader(f"Indikaattorin '{selected_indicator}' vertailu eri alueilla")
st.bar_chart(df_detailed[selected_indicator])

# Yksityiskohtainen tarkastelu valitusta indikaattorista ja alueesta
st.subheader(f"Aluekohtainen tulos: {selected_region} - {selected_indicator}")
indicator_score = df_detailed.loc[selected_region, selected_indicator]
st.metric(f"{selected_region} - {selected_indicator}", indicator_score)

# Näytä kaikki indikaattorit
st.header("Kaikki indikaattorit")
st.dataframe(df_detailed)

# Yhteenveto ja kehityssuositukset
st.header("Yhteenveto ja Kehityssuositukset")
st.markdown("""
- **Politiikka:** Lisää koulutusta ja strategista ohjeistusta.
- **Portaali:** Varmista datan käytettävyys ja ajantasaisuus.
- **Laatu:** Paranna datan tarkkuutta ja anonymisointia.
- **Vaikuttavuus:** Seuraa datan käyttöastetta ja käyttäjäpalautetta.
""")
