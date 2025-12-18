Fraud Awareness & Prevention Web App

OVERVIEW

This project is a local web-based application designed to raise public awareness
about fraud and provide basic tools for early detection and reporting of scam
attempts.

The application is intended as an educational / pilot project and focuses on
fraud prevention rather than law enforcement. It is implemented using Python
and Streamlit and runs fully locally without external services.

--------------------------------------------------

PURPOSE

Fraud-related crimes are increasing, while still remaining relatively rare and
often underestimated by the general public. Many victims fall for scams due to:

- Lack of awareness about fraud methods
- Limited technical or digital literacy

This application aims to:
- Educate users about common fraud schemes
- Provide a simple “quick check” tool for suspicious data
- Allow anonymous reporting of suspected fraud attempts
- Support preventive and informational campaigns

--------------------------------------------------

KEY FEATURES
------------

1. Fraud Information Page
   - Overview of current fraud trends
   - Explanation of the most common scam types

2. Common Fraud Methods
   - Step-by-step explanation of how scams are typically carried out
   - Behavioral manipulation techniques (urgency, fear, authority)
   - Examples relevant to real-world situations

3. Quick Check Tool (Rule-Based Detector)
   - Allows users to check:
     * Phone numbers
     * Domains

4. Incident Reporting (Demo Mode)
   - Simple form for reporting suspected fraud attempts
   - Serves as a conceptual model for future integration with official systems

--------------------------------------------------

TARGET AUDIENCE
- General public
- Senior citizens
- Students
- Community prevention groups

--------------------------------------------------

TECHNOLOGY STACK
----------------
- Python 3.10+
- Streamlit
- No external APIs or databases
- Fully local execution

--------------------------------------------------

RUNNING THE APPLICATION
-----------------------
1. Install Python (Anaconda recommended)
2. Create and activate a virtual environment
3. Install dependencies:
   pip install streamlit
4. Run the application:
   streamlit run app.py
5. Open the browser at designated localhost.

--------------------------------------------------

LIMITATIONS
-----------
- Fraud detection is rule-based and not exhaustive
- Blacklists are static and for demonstration purposes only
- The application does not replace official police or banking systems

--------------------------------------------------

ETHICAL AND LEGAL DISCLAIMER
----------------------------
This application is intended for educational and preventive purposes only.
It does not provide legal advice and does not guarantee detection of all fraud
attempts.

Users should always:
- Contact their bank immediately in case of financial risk
- Report confirmed incidents to the police using official channels

--------------------------------------------------


AUTHOR

Developed as part of a challenge-based academic project focused on fraud
awareness and prevention.
