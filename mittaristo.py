import streamlit as st
import pandas as pd
import numpy as np

# Mock data for visualization
regions = ["Pohjois-Pohjanmaa", "Pirkanmaa", "Varsinais-Suomi", "Uusimaa", "Lapland"]
indicators = {
    "Politiikka": ["Avoimen datan strategia", "Lainsäädännön noudattaminen", "Koulutus ja tuki"],
    "Portaali": ["Portaalin käytettävyys", "Teknologinen infrastruktuuri", "Avoimuuden indikaattorit"],
    "Laatu": ["Datan täydellisyys", "Datan tarkkuus", "Anonymisointi"],
    "Vaikuttavuus": ["Datan käyttöaste", "Käyttäjäpalaute", "Talousvaikutukset"]
}

# Generate random scores for each indicator
data = {}
for category, questions in indicators.items():
    for question in questions:
        data[question] = np.random.randint(50, 100, size=len(regions))

# Create DataFrame
df = pd.DataFrame(data, index=regions)

# Streamlit App Layout
st.title("Hyvinvointialueiden Avoimuus -Mittarist")
st.markdown("""
Tämä mittaristo perustuu Open Data Maturity Index -mittaristoon ja Open Knowledge Finlandin tekemään tutkimukseen, jonka tavoitteena on auttaa hyvinvointialueita avoimuuden mittaroinnissa.
Tämä mittaristo visualisoi hyvinvointialueiden avoimen datan kypsyyden neljässä pääkategoriassa: 
- **Politiikka**
- **Portaali**
- **Laatu**
- **Vaikuttavuus**

Voit valita tietyn alueen ja indikaattorin tarkasteluun sekä verrata indikaattorin arvoja eri alueiden kesken.
""")
# Valitse indikaattori
selected_category = st.selectbox("Valitse kategoria", list(indicators.keys()))
selected_question = st.selectbox("Valitse indikaattori", indicators[selected_category])

# Näytä valitun indikaattorin tulokset
st.header(f"Indikaattorin '{selected_question}' vertailu eri alueilla")
st.bar_chart(df[selected_question])

# Yksityiskohtainen tarkastelu
st.header("Aluekohtainen tulos")
selected_region = st.selectbox("Valitse hyvinvointialue", regions)
region_score = df.loc[selected_region, selected_question]
st.metric(f"{selected_region} - {selected_question}", region_score)

# Näytä koko data DataFrame-muodossa
st.header("Kaikki indikaattorit")
st.dataframe(df)

# Yhteenveto ja kehityssuositukset
st.header("Yhteenveto ja Kehityssuositukset")
st.markdown("""
- **Politiikka:** Lisää koulutusta ja strategista ohjeistusta.
- **Portaali:** Varmista datan käytettävyys ja ajantasaisuus.
- **Laatu:** Paranna datan tarkkuutta ja anonymisointia.
- **Vaikuttavuus:** Seuraa datan käyttöastetta ja käyttäjäpalautetta.
""")
