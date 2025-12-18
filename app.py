import streamlit as st
import datetime
from pathlib import Path

# --------------------------------------------------
# PAGRINDINIAI NUSTATYMAI
# --------------------------------------------------
st.set_page_config(
    page_title="Sukčiavimų prevencijos portalas",
    layout="wide"
)

# --------------------------------------------------
# FAILŲ KELIAI (GitHub / Streamlit Cloud friendly)
# --------------------------------------------------
BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "assets" / "fraubusterslogo.png"

# --------------------------------------------------
# NAVIGACIJA
# --------------------------------------------------
st.sidebar.title("🔍 Navigacija")
page = st.sidebar.radio(
    "Pasirinkite puslapį:",
    [
        "Apie sukčiavimus",
        "Dažniausi būdai",
        "Greitas patikrinimas",
        "Pranešti atvejį"
    ]
)

# Sidebar branding
st.sidebar.markdown("---")
st.sidebar.caption("FraudBusters – prevencijos projektas")

# --------------------------------------------------
# STILIUS
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #fafafa;
}
.info-box {
    background: #f8f9fa;
    border-left: 4px solid #2c7be5;
    padding: 12px;
    margin-bottom: 12px;
}
h1, h2, h3 {
    color: #2c3e50;
}
.warning {
    color: #b52b2b;
    font-weight: bold;
}
input, textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DEMO DUOMENYS (BLACKLIST)
# --------------------------------------------------
BLACKLIST = {
    "phones": [
        "+37060000000",
        "+37061112222"
    ],
    "domains": [
        "seb-bank-login.net",
        "fake-investment.lt",
        "vmi-secure.com"
    ],
    "ibans": [
        "LT601010051234567890"
    ]
}

# --------------------------------------------------
# 1. APIE SUKČIAVIMUS
# --------------------------------------------------
if page == "Apie sukčiavimus":
    st.title("Sukčiavimų prevencijos informacija")

    # Centruotas logotipas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(LOGO_PATH), width=260)

    st.markdown("""
Sukčiavimai Lietuvoje išlieka viena sparčiausiai augančių nusikalstamų veikų rūšių.  
Pagal naujausius duomenis:

- **Telefoniniai sukčiavimai** padidėjo beveik 3 kartus  
- **Kibernetiniai (interneto) sukčiavimai** – beveik 2 kartus  
- **Investiciniai sukčiavimai** – daugiau nei dvigubai  

Didžioji dalis sukčiavimų vyksta per:
- telefoninius skambučius,
- SMS žinutes,
- socialinius tinklus,
- klastotas interneto svetaines.

Sukčiai dažnai apsimeta:
- policijos ar banko darbuotojais,
- ryšio operatoriais,
- draudimo ar energijos tiekimo įmonėmis.

Jų pagrindinis tikslas – išgauti prisijungimus prie el. bankininkystės, priversti atlikti pavedimus
arba išvilioti grynuosius pinigus.
""")

    st.info(
        "💡 Policijos rekomendacija: niekada nesidalinkite prisijungimais, PIN kodais ar "
        "banko kortelės duomenimis. Policija ir bankai NIEKADA jų neprašo."
    )

# --------------------------------------------------
# 2. DAŽNIAUSI BŪDAI
# --------------------------------------------------
elif page == "Dažniausi būdai":
    st.title("⚠️ Dažniausi sukčiavimo būdai")

    st.markdown("""
**1️⃣ Telefoninis sukčiavimas**  
Skambinama apsimetus banko ar policijos darbuotoju. Prašoma „patikrinti sąskaitą“,
„atnaujinti sutartį“ ar įdiegti nuotolinės prieigos programą (pvz., AnyDesk).

**2️⃣ Kibernetinis sukčiavimas (phishing)**  
Siunčiami el. laiškai ar žinutės su nuorodomis į klastotas svetaines
(*SEB*, *VMI*, *DPD*, *Ignitis*, *Omniva*).

**3️⃣ Avansiniai mokėjimai**  
Fiktyvūs skelbimai apie butų nuomą, darbus ar pigias prekes.
Pinigai sumokami iš anksto, tačiau prekės ar paslaugos nesuteikiamos.

**4️⃣ Investiciniai sukčiavimai**  
Siūlomos „garantuotos“ investicijos, dažnai susijusios su kriptovaliutomis.
Aukos skatinamos pervesti lėšas ar imti paskolas.

**5️⃣ Romantiniai ir socialiniai sukčiavimai**  
Užmezgamas ilgalaikis emocinis ryšys, po kurio prašoma pinigų
„kritinei situacijai“ ar „pagalbai“.
""")

    st.success(
        "✅ Jei pasiūlymas atrodo per geras, kad būtų tikras – labai tikėtina, kad tai sukčiavimas."
    )

# --------------------------------------------------
# 3. GREITAS PATIKRINIMAS
# --------------------------------------------------
elif page == "Greitas patikrinimas":
    st.title("🔎 Greitas įtartino elemento patikrinimas")

    st.markdown(
        "Įveskite telefono numerį, domeną arba IBAN, kad patikrintumėte, "
        "ar jis pasitaiko žinomų sukčiavimo atvejų sąrašuose."
    )

    input_type = st.radio(
        "Ką norite patikrinti:",
        ["Telefono numeris", "Domenas", "IBAN"]
    )

    user_input = st.text_input("Įveskite reikšmę:")

    if st.button("Tikrinti"):
        value = user_input.strip().lower()

        if not value:
            st.warning("Įveskite reikšmę.")
        else:
            found = False

            if input_type == "Telefono numeris":
                found = value in [x.lower() for x in BLACKLIST["phones"]]
            elif input_type == "Domenas":
                found = value in [x.lower() for x in BLACKLIST["domains"]]
            elif input_type == "IBAN":
                found = value in [x.lower() for x in BLACKLIST["ibans"]]

            if found:
                st.error(
                    "🚨 Ši reikšmė sutampa su žinomu sukčiavimo atveju. "
                    "Rekomenduojama nutraukti bet kokį bendravimą."
                )
            else:
                st.success(
                    "✅ Šaltiniuose ši reikšmė neaptikta. "
                    "Vis tiek būkite budrūs ir patikrinkite informaciją papildomai."
                )

# --------------------------------------------------
# 4. PRANEŠTI ATVEJĮ
# --------------------------------------------------
elif page == "Pranešti atvejį":
    st.title("📩 Pranešti apie galimą sukčiavimą")

    with st.form("fraud_report_form"):
        name = st.text_input("Vardas, pavardė (nebūtina):")
        contact = st.text_input("El. paštas arba tel. numeris (nebūtina):")
        fraud_type = st.selectbox(
            "Koks tai buvo sukčiavimo tipas?",
            [
                "Telefoninis skambutis",
                "Interneto / el. laiškas",
                "SMS žinutė",
                "Kitas"
            ]
        )
        description = st.text_area("Trumpai aprašykite situaciją:")
        date = st.date_input("Įvykio data:", datetime.date.today())

        submitted = st.form_submit_button("Pateikti pranešimą")

        if submitted:
            st.session_state.setdefault("reports", []).append({
                "name": name,
                "contact": contact,
                "fraud_type": fraud_type,
                "description": description,
                "date": str(date)
            })
            st.success(
                "✅ Ačiū! Jūsų pranešimas užregistruotas. "
                "Jis gali būti panaudotas prevencinei analizei."
            )

    if st.session_state.get("reports"):
        st.write("### 🗂️ Pateikti pranešimai (demo režimas):")
        st.dataframe(st.session_state["reports"])
