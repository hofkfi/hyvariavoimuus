import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
        "Keusote / Tietojohtajan sähköposti", 
        "Avoindata.fi (HUS ostolaskut)", "Avoindata.fi",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ]
}

# Luodaan DataFrame
df = pd.DataFrame(data)

# Streamlit-sovellus
st.title("Hyvinvointialueiden Ostolaskudatan Julkaisutilanne 2025")
st.markdown("Päivitetty lista Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteesta maaliskuussa 2025.")

# Kokonaiskuva julkaisutilanteesta
st.header("Kokonaiskuva Julkaisutilanteesta")
st.bar_chart(df['Julkaistu?'].value_counts())

# Yksittäisen alueen tarkastelu
st.header("Yksittäisen Hyvinvointialueen Tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", df["Hyvinvointialue / Erityisyksikkö"])

region_data = df[df["Hyvinvointialue / Erityisyksikkö"] == selected_region]

st.subheader(f"Julkaisutilanne: {selected_region}")
st.markdown(f"- **Julkaistu?**: {region_data['Julkaistu?'].values[0]}")
st.markdown(f"- **Vuosi**: {region_data['Vuosi'].values[0]}")
st.markdown(f"- **Muoto**: {region_data['Muoto'].values[0]}")
st.markdown(f"- **Lähde**: {region_data['Lähde'].values[0]}")

# Vertaileva analyysi suhteessa muihin
st.header("Alueen Julkaisutilanne Suhteessa Muihin")
fig1, ax1 = plt.subplots()
df['Julkaistu?'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'orange'], ax=ax1)
ax1.set_title("Julkaisujen Osuus Kaikista Alueista")
ax1.set_ylabel("")
st.pyplot(fig1)

# Muodon vertailu suhteessa muihin
st.header("Muodon Vertailu Suhteessa Muihin Alueisiin")
fig2, ax2 = plt.subplots()
df['Muoto'].value_counts().plot(kind='bar', color='blue', ax=ax2)
ax2.set_title("Julkaisumuotojen Jakautuminen")
ax2.set_xlabel("Julkaisumuoto")
ax2.set_ylabel("Hyvinvointialueiden määrä")
st.pyplot(fig2)

# Lähteiden vertailu suhteessa muihin
st.header("Lähteiden Vertailu Suhteessa Muihin Alueisiin")
fig3, ax3 = plt.subplots()
df['Lähde'].value_counts().plot(kind='bar', color='purple', ax=ax3)
ax3.set_title("Lähteiden Jakautuminen")
ax3.set_xlabel("Lähde")
ax3.set_ylabel("Hyvinvointialueiden määrä")
st.pyplot(fig3)

# Yhteenveto ja kehitysehdotukset
st.header("Yhteenveto ja Kehitysehdotukset")
st.markdown("""
- **Aluekohtainen näkyvyys:** Tarvetta parantaa aluekohtaisen datan julkistamista.
- **Yhtenäiset käytännöt:** Datan muoto ja julkaisutapa tulisi harmonisoida.
- **Keskitetyt julkaisualustat:** Yhtenäinen julkaisu esimerkiksi Avoindata.fi-portaalissa parantaisi löydettävyyttä.
""")
