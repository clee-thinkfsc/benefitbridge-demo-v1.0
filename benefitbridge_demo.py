import streamlit as st
import pandas as pd
import json
import os

# Load contacts
if os.path.exists("sample_contacts_expanded.csv"):
    contacts = pd.read_csv("sample_contacts_expanded.csv")
else:
    contacts = pd.DataFrame(columns=[
        "First Name", "Last Name", "Medicaid ID", "SSN Last 4", "Date of Birth",
        "Street", "City", "State", "Zip", "Mailing Street", "Mailing City",
        "Mailing State", "Mailing Zip", "Cell Phone", "Email", "Alt Phone"
    ])

# Load locales
if os.path.exists("locales.json"):
    with open("locales.json", "r") as f:
        locales = json.load(f)
else:
    locales = {"languages": ["English"]}

# Session state for chatbot
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "step" not in st.session_state:
    st.session_state.step = 0
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

st.title("🤝 BenefitBridge AI Demo")
st.markdown("A friendly Louisiana social worker chatbot helping with Medicaid contact updates & income verification.")

# Display chat history
for role, text in st.session_state.chat_history:
    if role == "bot":
        st.chat_message("assistant").write(text)
    else:
        st.chat_message("user").write(text)

# Bot script flow
script = [
    "Hi! I'm your friendly Louisiana BenefitBridge assistant. Let's start by selecting your language.",
    f"Available languages: {', '.join(locales['languages'])}. Please type your choice.",
    "Great. What name would you like me to call you?",
    "Please confirm by typing your full name that you give the Louisiana Dept. of Health permission to verify your information.",
    "Enter your First Name:",
    "Enter your Last Name:",
    "Enter your Medicaid ID (optional):",
    "Enter last 4 digits of your SSN:",
    "Enter your Date of Birth (YYYY-MM-DD):",
    "Please enter the verification code sent to your phone.",
    "Here is your current contact information on file. What would you like to update? (home, mailing, phone, email)",
    "Enter new Home Address Street:",
    "Enter City:",
    "Enter State:",
    "Enter Zip:",
    "Enter Mailing Address Street (or 'same'):",
    "Enter Mailing City:",
    "Enter Mailing State:",
    "Enter Mailing Zip:",
    "Enter Cell Phone:",
    "Enter Email:",
    "Enter Alternative Phone:",
    "How would you like to be contacted in the future? (text, email, phone)",
    "Would you like to verify your income now? (yes/no)",
    "If yes: please upload your documents."
]

# Handle user input
if user_input := st.chat_input("Type your message here..."):
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.form_data[f"step_{st.session_state.step}"] = user_input

    st.session_state.step += 1
    if st.session_state.step < len(script):
        bot_msg = script[st.session_state.step]
    else:
        bot_msg = "Thank you! Your updates have been submitted."

    st.session_state.chat_history.append(("bot", bot_msg))
    st.experimental_rerun()
