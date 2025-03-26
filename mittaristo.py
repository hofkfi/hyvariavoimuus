import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
st.title("Hyvinvointialueiden avoimuus -mittaristo")
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
st.header("Mittariston kokonaiskuva")
st.bar_chart(df_summary)

# Yksityiskohtainen aluekohtainen tarkastelu
st.header("Yksityiskohtainen aluekohtainen tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", regions)
region_data = df_summary.loc[selected_region]

st.subheader(f"Hyvinvointialue: {selected_region}")
st.metric("Politiikka", region_data["Politiikka"])
st.metric("Portaali", region_data["Portaali"])
st.metric("Laatu", region_data["Laatu"])
st.metric("Vaikuttavuus", region_data["Vaikuttavuus"])

# Indikaattorin vertailu eri alueiden välillä
st.header("Indikaattorin vertailu")
selected_category = st.selectbox("Valitse kategoria", list(indicators.keys()))
selected_indicator = st.selectbox("Valitse indikaattori", indicators[selected_category])

st.subheader(f"Indikaattorin '{selected_indicator}' vertailu eri alueilla")
st.bar_chart(df_detailed[selected_indicator])

# Chatbot-toiminto
st.header("Chatbot: kysy mittaristosta")
user_input = st.text_input("Kysy kysymys mittaristosta:")

def chatbot_response(question):
    question = question.lower()

    # Yleistiedustelut
    if "kokonaiskuva" in question:
        return "Kokonaiskuva näyttää eri alueiden suoriutumisen neljässä pääkategoriassa: politiikka, portaali, laatu ja vaikuttavuus."
    
    # Aluekohtaiset kysymykset
    for region in regions:
        if region.lower() in question:
            region_data = df_summary.loc[region]
            response = f"Alue {region}:\n"
            response += f"- Politiikka: {region_data['Politiikka']}\n"
            response += f"- Portaali: {region_data['Portaali']}\n"
            response += f"- Laatu: {region_data['Laatu']}\n"
            response += f"- Vaikuttavuus: {region_data['Vaikuttavuus']}\n"
            return response
    
    # Indikaattorikohtaiset kysymykset
    for indicator in df_detailed.columns:
        if indicator.lower() in question:
            values = df_detailed[indicator]
            avg_value = values.mean()
            max_value = values.max()
            min_value = values.min()
            max_region = values.idxmax()
            min_region = values.idxmin()
            response = f"Indikaattori '{indicator}':\n"
            response += f"- Keskimääräinen arvo: {avg_value:.2f}\n"
            response += f"- Korkein arvo: {max_value} ({max_region})\n"
            response += f"- Matalin arvo: {min_value} ({min_region})\n"
            return response
    
    return "En ymmärtänyt kysymystäsi. Yritä uudelleen!"

# Näytä chatbotin vastaus
if user_input:
    response = chatbot_response(user_input)
    st.write(f"🗣️ **Chatbot:** {response}")

# Näytä kaikki indikaattorit
st.header("Kaikki indikaattorit")
st.dataframe(df_detailed)

# Ohjeet ja lähteet
st.header("Ohjeet ja lähteet")
st.markdown("""
- **Avoindata.fi-portaali**: Suomen kansallinen avoimen datan portaali. [Avoindata.fi](https://www.avoindata.fi)
- **Kuntaliiton ohje ostolaskujen avaamisesta**: Ohje kunnille ostolaskujen julkaisemiseksi avoimena datana. [Kuntaliiton ohje](https://www.kuntaliitto.fi/ajankohtaista/2016/kunnille-ohje-ostolaskujen-avaamisesta-avoimena-datana)
- **Open Data Maturity Index**: Euroopan komission raportti avoimen datan kypsyydestä. [Open Data Maturity Index](https://data.europa.eu/en/publications/open-data-maturity)
""")

# Yhteenveto ja kehityssuositukset
st.header("Yhteenveto ja kehityssuositukset")
st.markdown("""
- **Politiikka**: Lisää koulutusta ja strategista ohjeistusta.
- **Portaali**: Varmista datan käytettävyys ja ajantasaisuus.
- **Laatu**: Paranna datan tarkkuutta ja anonymisointia.
- **Vaikuttavuus**: Seuraa datan käyttöastetta ja käyttäjäpalautetta.
""")
