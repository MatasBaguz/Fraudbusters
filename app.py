import streamlit as st
import datetime

# --- Puslapio nustatymai ---
st.set_page_config(page_title="Sukčiavimų prevencijos portalas", layout="wide")

# --- Navigacija ---
st.sidebar.title("🔍 Navigacija")
page = st.sidebar.radio(
    "Pasirinkite puslapį:",
    ["Apie sukčiavimus", "Dažniausi būdai", "Greitas patikrinimas", "Pranešti atvejį"]
)

# --- Stilius ---
st.markdown("""
<style>
body { background-color: #fafafa; }
.info-box {
  background: #f8f9fa;
  border-left: 4px solid #2c7be5;
  padding: 12px;
  margin-bottom: 12px;
}
h2, h3 { color: #2c3e50; }
.warning { color: #b52b2b; font-weight: bold; }
input, textarea { font-size: 16px !important; }
</style>
""", unsafe_allow_html=True)

# --- Duomenys testavimui ---
BLACKLIST = {
    "phones": ["+37060000000", "+37061112222"],
    "domains": ["seb-bank-login.net", "fake-investment.lt", "vmi-secure.com"],
    "ibans": ["LT601010051234567890"]
}

# --- 1. Apie sukčiavimus ---
if page == "Apie sukčiavimus":
    st.title("🛡️ Sukčiavimų prevencijos informacija")
    st.markdown("""
Sukčiavimai Lietuvoje išlieka viena sparčiausiai augančių nusikalstamų veikų rūšių.  
Pagal 2025 m. duomenis:
- **Telefoniniai sukčiavimai** padidėjo beveik 3 kartus.
- **Kibernetiniai (interneto) sukčiavimai** – beveik 2 kartus.
- **Investiciniai apgaulės atvejai** – daugiau nei dvigubai.

Didžioji dalis sukčiavimų vyksta per **telefoninius skambučius, SMS žinutes, socialinius tinklus ir klastotas svetaines**.  
Sukčiai dažnai apsimeta:
- policijos arba banko darbuotojais,
- ryšio operatoriais,
- draudimo ar energijos tiekimo įmonėmis.

Pagrindinis jų tikslas – išgauti prisijungimus prie el. bankininkystės, priversti atlikti pervedimus arba perduoti grynuosius pinigus.
""")
    st.info("💡 Policijos rekomendacija: niekada nesidalinkite prisijungimais ar PIN kodais. Policija ir bankai NIEKADA jų neprašo.")

# --- 2. Dažniausi būdai ---
elif page == "Dažniausi būdai":
    st.title("⚠️ Dažniausi sukčiavimo būdai")
    st.markdown("""
**1️⃣ Telefoninis sukčiavimas**  
Skambinama apsimetus banko ar policijos darbuotoju. Prašoma „patikrinti sąskaitą“, „atnaujinti sutartį“, „įdiegti programėlę“ (pvz., AnyDesk).

**2️⃣ Kibernetinis sukčiavimas (phishing)**  
Siunčiami el. laiškai ar žinutės su nuorodomis į suklastotas svetaines: *SEB*, *VMI*, *DPD*, *Ignitis*, *Omniva*.

**3️⃣ Avansiniai mokėjimai**  
Skelbimai apie fiktyvų butų nuomą, darbus, pigias prekes. Pinigai pervedami iš anksto, prekės – neegzistuoja.

**4️⃣ Investiciniai sukčiavimai**  
„Finansų konsultantai“ ar „kriptovaliutų ekspertai“ siūlo investuoti. Auka prašoma pervesti lėšas ar paimti kreditą investicijoms.

**5️⃣ Romantiniai / socialiniai sukčiavimai**  
Sukčiai apsimeta draugais, partneriais, net kariškiais, palaiko ryšį kelias savaites, vėliau prašo pinigų „gelbėjimui“.
""")
    st.success("✅ Atminkite: jei skambutis, žinutė ar pasiūlymas kelia įtarimą – nutraukite kontaktą ir pasitarkite su artimaisiais ar policija.")

# --- 3. Greitas patikrinimas ---
elif page == "Greitas patikrinimas":
    st.title("🔎 Greitas įtartino elemento patikrinimas")

    st.markdown("Įveskite telefono numerį, IBAN arba domeną, kad patikrintumėte, ar jis pasitaiko žinomų sukčiavimų sąrašuose.")

    input_type = st.radio("Ką norite patikrinti:", ["Telefono numeris", "Domenas", "IBAN"])

    user_input = st.text_input("Įveskite reikšmę:")

    if st.button("Tikrinti"):
        result = "neutral"
        value = user_input.strip().lower()

        if not value:
            st.warning("Įveskite reikšmę.")
        else:
            if input_type == "Telefono numeris":
                if value in [x.lower() for x in BLACKLIST["phones"]]:
                    result = "danger"
            elif input_type == "Domenas":
                if value in [x.lower() for x in BLACKLIST["domains"]]:
                    result = "danger"
            elif input_type == "IBAN":
                if value in [x.lower() for x in BLACKLIST["ibans"]]:
                    result = "danger"

            if result == "danger":
                st.error("🚨 Ši reikšmė sutampa su žinomu sukčiavimo atveju! Nedelsdami būkite atsargūs.")
            else:
                st.success("✅ Šaltiniuose ši reikšmė neaptikta. Vis tiek būkite budrūs, patikrinkite siuntėją ar numerį papildomai.")

# --- 4. Pranešti atvejį ---
elif page == "Pranešti atvejį":
    st.title("📩 Pranešti apie galimą sukčiavimą")

    with st.form("fraud_report_form"):
        name = st.text_input("Vardas, pavardė (nebūtina):")
        contact = st.text_input("El. paštas arba tel. numeris (nebūtina):")
        fraud_type = st.selectbox(
            "Koks tai buvo sukčiavimo tipas?",
            ["Telefoninis skambutis", "Interneto / el. laiškas", "SMS žinutė", "Kitas"]
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
            st.success("✅ Ačiū! Jūsų pranešimas užregistruotas. Policijos pareigūnai galės juo pasinaudoti prevencijai.")

    if st.session_state.get("reports"):
        st.write("### 🗂️ Jūsų pateikti pranešimai (demo režimu):")
        st.dataframe(st.session_state["reports"])
