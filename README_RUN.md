
# BenefitBridge AI — Quick Demo Prototype

This package contains a lightweight, **click-through prototype** to demonstrate how BenefitBridge AI would streamline Louisiana's Medicaid Unwind workflow.

## What's Included
- `mock_recipients.csv` — de-identified mock LDH records (10 sample recipients)
- `sms_templates.csv` — English/Spanish reminder templates
- `benefitbridge_demo.py` — Streamlit app (recipient flow + LDH dashboard)
- `requirements.txt` — minimal dependencies
- `README_RUN.md` — how to run

## How to Run (Local)
1. Create and activate a virtual environment (optional but recommended).
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```bash
   streamlit run benefitbridge_demo.py
   ```
4. The app will open in your browser. Use **Recipient Flow** to update contact info, then switch to **Caseworker Dashboard** to see KPIs and events.

## What to Demo
- **Recipient Flow:** identity match, address suggestion, update submission, SMS opt-in.
- **LDH Dashboard:** today's updates, at-risk counts, reach rate, and "Need Attention" flags.

## Notes
- All data is mock and for demonstration only.
- Messaging is simulated; no real SMS is sent.
- You can expand this by adding OCR for document capture and a simple rules API for verifications.
