import streamlit as st
import pandas as pd
import numpy as np

# Sivuasetukset
st.set_page_config(page_title="Open Data Maturity", layout="wide")

# Sidebar: ohjeet ja linkit
with st.sidebar:
    st.title("📚 Ohjeet ja linkit")
    st.markdown("""
    **🔗 Kuntaliiton ohjeistus:**  
    [Kuntien ja kuntayhtymien ostolaskudatan avaamisen ohje (2021)](https://www.kuntaliitto.fi/julkaisut/2021/2112-kuntien-ja-kuntayhtymien-ostolaskudatan-avaamisen-ohje)

    **🌐 Avoindata.fi Julkaisijan opas:**  
    [Avoindata.fi - Julkaisijan ohjeet](https://www.avoindata.fi/fi/kayttoohjeet)

    **🧰 Työkalut:**
    - [Open Data Editor (ODE)](https://opendataeditor.okfn.org/)  
    - [DCAT-AP Validator](https://www.dcat-ap-validator.eu/)  
    """)

# Mock-data (voit korvata oikealla datalla)
regions = [
    "Varsinais-Suomi", "Pirkanmaa", "Pohjois-Pohjanmaa",
    "Keski-Uusimaa", "Pohjois-Savo", "Etelä-Savo",
    "Päijät-Häme", "Kainuu", "Keski-Suomi", "Etelä-Pohjanmaa",
    "Satakunta", "Pohjanmaa", "Kanta-Häme", "Itä-Uusimaa",
    "Länsi-Uusimaa", "Lappi", "Vantaa ja Kerava", "Pohjois-Karjala",
    "Keski-Pohjanmaa", "Etelä-Karjala"
]

categories = ["Politiikka", "Portaali", "Laatu", "Vaikuttavuus"]
np.random.seed(42)
data = np.random.randint(20, 100, size=(len(regions), len(categories)))
df = pd.DataFrame(data, index=regions, columns=categories)

# Titteli
st.title("Hyvinvointialueiden Open Data Maturity -Mittaristo")
st.markdown("Visualisointi hyvinvointialueiden avoimen datan kypsyydestä neljässä pääkategoriassa (Mock-up datalla):")

# Selitys
with st.expander("ℹ️ Mittariston selitys"):
    st.markdown("""
    - **Politiikka**: Strateginen ohjeistus, lainsäädännön huomiointi
    - **Portaali**: Avoindata.fi:n tai vastaavan käytettävyys ja tekninen taso
    - **Laatu**: Datan tarkkuus, anonymisointi, metadata
    - **Vaikuttavuus**: Datan käyttö, hyödyntäminen ja näkyvyys yhteiskunnassa
    """)

# Visualisointi: bar chart
st.subheader("📊 Aluekohtainen vertailu (bar chart)")
st.bar_chart(df)

# Interaktiivinen aluevalinta
st.subheader("🔍 Alueen tarkempi tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", df.index.tolist())
region_data = df.loc[selected_region]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Politiikka", region_data["Politiikka"])
col2.metric("Portaali", region_data["Portaali"])
col3.metric("Laatu", region_data["Laatu"])
col4.metric("Vaikuttavuus", region_data["Vaikuttavuus"])

# Suositukset
st.subheader("✅ Kehityssuositukset")
st.markdown(f"""
**{selected_region}**:
- 💼 Politiikka: { "Hyvällä tasolla" if region_data["Politiikka"] > 60 else "Vaatii vahvistusta" }
- 🌐 Portaali: { "Käytettävyys kunnossa" if region_data["Portaali"] > 60 else "Teknistä kehitystä tarvitaan" }
- 📊 Laatu: { "Metadata ja anonymisointi ok" if region_data["Laatu"] > 60 else "Laadunhallinta kaipaa panostusta" }
- 💡 Vaikuttavuus: { "Data näkyy ja vaikuttaa" if region_data["Vaikuttavuus"] > 60 else "Lisää käyttöä ja näkyvyyttä" }
""")
