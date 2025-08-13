
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="BenefitBridge AI Demo", layout="wide")

@st.cache_data
def load_data():
    recipients = pd.read_csv("mock_recipients.csv", parse_dates=["redet_due_date"])
    templates = pd.read_csv("sms_templates.csv")
    return recipients, templates

recipients, templates = load_data()

if "events" not in st.session_state:
    st.session_state.events = []  # simple event log

if "updates" not in st.session_state:
    st.session_state.updates = pd.DataFrame(columns=[
        "medicaid_id","name","updated_phone","updated_email","updated_address","ts","status"
    ])

st.sidebar.title("BenefitBridge AI Demo")
mode = st.sidebar.radio("Choose a demo:", ["Recipient Flow", "Caseworker Dashboard"])

# -------------- Recipient Flow --------------
if mode == "Recipient Flow":
    st.title("BenefitBridge for Louisiana Medicaid")
    st.write("Update your contact info in minutes to protect your coverage.")

    lang = st.radio("Language / Idioma", ["English","Español"])

    if lang == "Español":
        st.subheader("Verificación de Identidad")
        name = st.text_input("Nombre completo")
        dob = st.date_input("Fecha de nacimiento")
        med_id = st.text_input("ID de Medicaid (opcional)")
    else:
        st.subheader("Identity Verification")
        name = st.text_input("Full name")
        dob = st.date_input("Date of birth")
        med_id = st.text_input("Medicaid ID (optional)")

    if st.button("Find my record / Buscar mi registro"):
        m = None
        # Try med_id match first; fallback to name+dob
        if med_id:
            m = recipients[recipients["medicaid_id"] == med_id]
        if m is None or m.empty:
            # try name + dob string match
            m = recipients[(recipients["name"].str.lower()==name.strip().lower())]
        if m.empty:
            st.error("No matching record found. Please check your info.")
        else:
            rec = m.iloc[0].copy()
            st.success("Record found.")
            st.write("**On file:**")
            st.write(f"- Phone: {rec['phone']}  \n- Email: {rec['email']}  \n- Address: {rec['address_old']}")
            st.info(f"Suggested new address (USPS): {rec['address_candidate']}")
            st.session_state.current_rec = rec.to_dict()

    if "current_rec" in st.session_state:
        rec = st.session_state.current_rec
        st.subheader("Confirm or Update Contact Info")

        new_phone = st.text_input("Phone", value=rec["phone"])
        new_email = st.text_input("Email", value=rec["email"])
        new_addr  = st.text_area("Address", value=rec["address_candidate"])

        sms_opt = st.checkbox("Get text reminders about my renewal")
        due = pd.to_datetime(rec["redet_due_date"]).date()
        st.write(f"**Your renewal is due on:** {due}")

        if st.button("Send Update to LDH"):
            ts = datetime.utcnow().isoformat()
            st.session_state.updates.loc[len(st.session_state.updates)] = [
                rec["medicaid_id"], rec["name"], new_phone, new_email, new_addr, ts, "posted_200"
            ]
            st.session_state.events.append({"ts": ts, "type": "ldh_intake_posted", "medicaid_id": rec["medicaid_id"]})
            if sms_opt:
                st.session_state.events.append({"ts": ts, "type": "sms_opt_in", "medicaid_id": rec["medicaid_id"]})
            st.success("LDH Update: Contact information submitted. You’ll receive reminders before your deadline.")
            st.balloons()

# -------------- Caseworker Dashboard --------------
else:
    st.title("LDH Caseworker Dashboard")

    # compute KPIs
    today = datetime.utcnow().date()
    completed = len(st.session_state.updates)
    at_risk = (recipients["redet_due_date"].dt.date - today).apply(lambda d: d.days <= 10).sum()
    reach_rate = 0
    # naive reach calc from events
    sms_opts = [e for e in st.session_state.events if e["type"]=="sms_opt_in"]
    attempts = max(len(st.session_state.events), 1)
    reach_rate = round(100*len(sms_opts)/attempts, 1)

    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Today's Updates", completed)
    kpi2.metric("At-risk (≤10 days)", at_risk)
    kpi3.metric("Reach Rate (demo)", f"{reach_rate}%")

    st.subheader("New / Updated")
    st.dataframe(st.session_state.updates)

    st.subheader("Need Attention")
    # simple flags: missing phone or nearing deadline
    rec_copy = recipients.copy()
    rec_copy["days_to_due"] = (rec_copy["redet_due_date"].dt.date - today).apply(lambda d: d.days)
    flags = rec_copy[(rec_copy["days_to_due"] <= 10) | (rec_copy["phone"].isna())][
        ["medicaid_id","name","phone","email","address_old","redet_due_date","days_to_due","risk_score"]
    ]
    st.dataframe(flags)

    st.caption("Demo only: data is mock and events are simulated in-session.")
