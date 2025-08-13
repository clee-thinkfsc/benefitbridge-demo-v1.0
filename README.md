
# BenefitBridge AI

BenefitBridge AI is a prototype chatbot designed to help Louisiana Medicaid recipients quickly and securely update their contact and income verification information during the Medicaid unwind process. The chatbot simulates integration with the Louisiana Department of Health (LDH) system and guides users through identity verification, contact updates, and income verification document submission.

---

## Features

- **Friendly Louisiana Social Worker Personality**: Creates a welcoming and supportive experience for recipients.
- **Multilingual Support**: English, Spanish, French, Vietnamese, Arabic, Chinese, Tagalog.
- **Secure Identity Verification**: Collects required identifying info and confirms via one-time passcode (OTP).
- **Contact Information Management**: Displays current information on file and allows updates to addresses, phone numbers, and email.
- **Preferred Contact Method Selection**: Text, Email, or Phone Call.
- **Income Verification Support**: Provides instructions for uploading verification documents based on chosen method.
- **Caseworker Escalation**: Routes complex questions to a caseworker callback queue.

---

## Conversation Flow

![BenefitBridge AI Conversation Flow](benefitbridge_flow_diagram.png)

### Steps:
1. Language selection.
2. Collect recipient’s name and identity verification details (Medicaid ID, SSN last 4, DOB).
3. Send OTP to the mobile number on file and validate.
4. Display current contact information from the LDH database.
5. Allow updates to home/mailing address, phone numbers, and email.
6. Collect preferred contact method for future verifications.
7. Offer immediate or scheduled income verification process.
8. Provide secure upload link or email/text instructions.
9. Escalate to caseworker if needed.

---

## Sample Data

The application includes a **sample_contacts.csv** file containing realistic mock recipient data with fields for:
- First & Last Name
- Medicaid ID
- SSN (last 4)
- Date of Birth
- Contact Info
- Preferred Contact Method

---

## Technology Stack

- **Python**
- **Streamlit** for the interactive web UI
- **Pandas** for handling sample contact data
- **Session State** for tracking user progress
- **GitHub** for version control
- **CSV** for mock recipient data

---

## Running the Demo

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/benefitbridge-ai.git
cd benefitbridge-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Security Considerations

In a production environment:
- Use secure authentication (OAuth, multi-factor).
- Encrypt all data in transit and at rest.
- Ensure database queries are parameterized and access-controlled.
- Store sensitive data in compliance with HIPAA.

---

## Future Enhancements

- Live API integration with Louisiana Department of Health systems.
- Secure document upload and storage.
- Expanded multilingual support with AI translation services.
- Detailed analytics dashboard for program administrators.

---

## License
MIT License
