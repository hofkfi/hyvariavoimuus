import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit asetukset
st.set_page_config(page_title="Ostolaskudata 2025", layout="wide")

# Kovakoodattu data
data = {
    "Hyvinvointialue": [
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
        "Dataset", "Excel", "Dataset (aineistossa)", 
        "Dataset (aineistossa)", "Excel", 
        "Power BI", "Dataset", "Excel",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ],
    "Lähde": [
        "Avoindata.fi", "paijatha.fi", "Tutkihankintoja.fi", 
        "Tutkihankintoja.fi", "etelasavonha.fi", 
        "keusote.fi", "Avoindata.fi", "Avoindata.fi",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa", "Ei tiedossa", "Ei tiedossa",
        "Ei tiedossa", "Ei tiedossa"
    ]
}

df = pd.DataFrame(data)

# Tyyli
plt.style.use("ggplot")
sns.set_palette("pastel")

# Sovelluksen sisältö
st.title("📊 Hyvinvointialueiden Ostolaskudatan Julkaisutilanne 2025")
st.markdown("Visualisointi ostolaskudatan avoimuudesta Suomessa. Tilannepäivitys: **maaliskuu 2025**.")

# Kokonaiskuva julkaisuista
st.subheader("1️⃣ Kokonaiskuva Julkaisutilanteesta")
col1, col2 = st.columns(2)

with col1:
    status_counts = df["Julkaistu"].value_counts()
    fig1, ax1 = plt.subplots()
    status_counts.plot.pie(autopct="%1.1f%%", labels=status_counts.index, colors=["lightgreen", "lightcoral"], ax=ax1)
    ax1.set_ylabel("")
    ax1.set_title("Julkaisujen Osuus")
    st.pyplot(fig1)

with col2:
    st.bar_chart(status_counts)

# Yksittäinen alue
st.subheader("2️⃣ Yksittäisen Hyvinvointialueen Tarkastelu")
selected = st.selectbox("Valitse alue", df["Hyvinvointialue"].tolist())
row = df[df["Hyvinvointialue"] == selected].iloc[0]
st.markdown(f"""
### 📍 {row['Hyvinvointialue']}
- **Julkaistu:** {row['Julkaistu']}
- **Vuosi:** {row['Vuosi'] if pd.notnull(row['Vuosi']) else '–'}
- **Muoto:** {row['Muoto']}
- **Lähde:** {row['Lähde']}
""")

# Muotojen vertailu
st.subheader("3️⃣ Julkaisumuotojen Jakautuminen")
fig2, ax2 = plt.subplots()
df["Muoto"].value_counts().plot(kind="bar", color="steelblue", ax=ax2)
ax2.set_ylabel("Alueiden määrä")
ax2.set_xlabel("Muoto")
ax2.set_title("Julkaisumuodot")
st.pyplot(fig2)

# Lähteiden vertailu
st.subheader("4️⃣ Lähteiden Jakautuminen")
fig3, ax3 = plt.subplots()
df["Lähde"].value_counts().plot(kind="bar", color="mediumpurple", ax=ax3)
ax3.set_ylabel("Alueiden määrä")
ax3.set_xlabel("Lähde")
ax3.set_title("Lähteet")
st.pyplot(fig3)

# Kehitysehdotukset
st.subheader("5️⃣ Yhteenveto ja Kehitysehdotukset")
st.markdown("""
- 📌 **Tarve yhtenäistää** tiedon muoto ja julkaisutapa (Excel vs Dataset vs BI-raportti)
- 🧭 **Keskitetyt julkaisualustat** (esim. Avoindata.fi tai Tutkihankintoja.fi) tukisivat löydettävyyttä
- 🤝 **Kokemusten jakaminen** voisi nopeuttaa hitaammin etenevien alueiden kehitystä
- 🧹 **Metadatan laatu** ja hakukategorisointi vaativat erityistä huomiota
""")
