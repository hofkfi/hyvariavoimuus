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
st.markdown("**Päivitetty lista Suomen hyvinvointialueiden ostolaskudatan julkaisutilanteesta maaliskuussa 2025.**")

# Kokonaiskuva julkaisutilanteesta
st.header("Kokonaiskuva Julkaisutilanteesta")

# Pylväsdiagrammi: Julkaisutilanne
st.subheader("Julkaisutilanne Hyvinvointialueittain")
fig1, ax1 = plt.subplots()
df['Julkaistu?'].value_counts().plot(kind='bar', color=['green', 'orange', 'red'], ax=ax1)
ax1.set_title("Julkaisutilanne")
ax1.set_xlabel("Julkaisu")
ax1.set_ylabel("Hyvinvointialueiden määrä")
st.pyplot(fig1)

# Piirakkadiagrammi: Julkaisut vs. Ei julkaisut
st.subheader("Julkaisut vs. Ei julkaisut")
fig2, ax2 = plt.subplots()
df['Julkaistu?'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'orange'], ax=ax2)
ax2.set_ylabel("")
ax2.set_title("Julkaisujen osuudet")
st.pyplot(fig2)

# Muotokohtainen jakautuminen
st.subheader("Julkaisujen Muotokohtainen Jakautuminen")
fig3, ax3 = plt.subplots()
df['Muoto'].value_counts().plot(kind='bar', color='blue', ax=ax3)
ax3.set_title("Julkaisujen Muotokohtainen Jakautuminen")
ax3.set_xlabel("Muoto")
ax3.set_ylabel("Määrä")
st.pyplot(fig3)

# Aluekohtainen tarkastelu
st.header("Aluekohtainen Tarkastelu")
selected_region = st.selectbox("Valitse hyvinvointialue", ["Kaikki"] + list(df["Hyvinvointialue / Erityisyksikkö"]))
if selected_region != "Kaikki":
    filtered_df = df[df["Hyvinvointialue / Erityisyksikkö"] == selected_region]
else:
    filtered_df = df

st.dataframe(filtered_df)

# Lähteiden jakautuminen
st.subheader("Lähteiden Jakautuminen")
fig4, ax4 = plt.subplots()
df['Lähde'].value_counts().plot(kind='bar', color='purple', ax=ax4)
ax4.set_title("Lähteiden Jakautuminen")
ax4.set_xlabel("Lähde")
ax4.set_ylabel("Määrä")
st.pyplot(fig4)

# Yhteenveto ja kehitysehdotukset
st.header("Yhteenveto ja Kehitysehdotukset")
st.markdown("""
- **Julkaisemattomat alueet:** Tarpeen saada lisää tietoa julkaisutilanteesta.
- **Yhtenäiset käytännöt:** Datan muoto ja julkaisukäytännöt tulisi yhdenmukaistaa.
- **Avoindata.fi-portaali:** Suositellaan keskitettyä julkaisua kansalliseen portaaliin.
- **Visualisointi ja tiedon hyödyntäminen:** Parannetaan julkisuusraportoinnin ja seurannan helppoutta.
""")
