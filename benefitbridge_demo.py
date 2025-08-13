import streamlit as st
import pandas as pd

# Load sample contacts
contacts = pd.read_csv('sample_contacts_expanded.csv')

st.set_page_config(page_title="BenefitBridge AI", page_icon="🤝", layout="centered")

st.title("🤝 BenefitBridge AI")
st.markdown("Your friendly Louisiana Medicaid assistant.")

# Language selection
language = st.selectbox("Select your preferred language:", 
    ["English", "Spanish", "French", "Vietnamese", "Arabic", "Chinese", "Tagalog"])

# User name
name = st.text_input("What name would you like to be called?")

# Legal acknowledgment
st.write("Please confirm by typing your full name below:")
ack_name = st.text_input("Full Name Confirmation")
if ack_name:
    st.success("Acknowledgment received.")

# Verification details
st.subheader("Verification Information")
first_name = st.text_input("First Name (Required)")
last_name = st.text_input("Last Name (Required)")
medicaid_id = st.text_input("Medicaid ID (Optional)")
ssn_last4 = st.text_input("Last 4 of SSN (Required)")
dob = st.date_input("Date of Birth (Required)")

# Mock verification step
if st.button("Send Verification Code"):
    st.info("A verification code has been sent to your mobile number on file. (Simulated)")

code_entered = st.text_input("Enter Verification Code")

# Display current contact info (simulated)
if st.button("Display Current Contact Info"):
    st.write("Simulated current contact information from database...")

# Update contact info
st.subheader("Update Contact Information")
update_field = st.selectbox("What would you like to update?", 
    ["Home Address", "Mailing Address", "Cell Phone Number", "Email Address", "Home Alternative Phone Number"])

st.text_input(f"New {update_field}")

# Contact preferences
contact_pref = st.radio("How do you want to be contacted in the future?", ["Text", "Email", "Phone Call"])

st.subheader("Income Verification")
verify_now = st.radio("Would you like to verify your income now?", ["Yes", "Remind me later"])

if verify_now == "Yes":
    st.write("Please upload your income verification document:")
    st.file_uploader("Upload File")
else:
    st.write("We will send you a reminder with the list of acceptable documents.")

st.success("Demo completed. This is a simulation — no actual Medicaid data is accessed.")
