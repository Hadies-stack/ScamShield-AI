# 🛡️ ScamShield AI

### An AI-Powered Digital Safety & Scam Detection Assistant

ScamShield AI is an AI-powered digital safety assistant designed to help users identify suspicious messages, recognise potential scam patterns, understand caller behaviour and improve cybersecurity awareness.

The project combines Machine Learning, rule-based threat detection and an interactive web interface to provide an accessible digital protection experience.

---

## 🚀 Key Features

### 1. Command Centre
- Central dashboard for navigating the application.
- Access to the different digital safety modules.

### 2. Cyber Safety
- Digital safety information and awareness.
- Guidance for recognising common online threats.

### 3. Scam Academy
- Educational content about scams and cybersecurity awareness.

### 4. Family Safety
- Digital safety guidance for families.

### 5. Link Safety
- Tool for checking suspicious URLs.

### 6. Threat Intelligence
- SMS threat analysis.
- Guided call behaviour analysis.
- Fraud risk score and risk level.
- Detection of suspicious patterns.
- Matched phrase identification.
- Recommended safety actions.
- Machine Learning-based SMS spam classification.

### 7. Threat Network
- Threat reporting and information exploration.

### 8. Market Insights
- Cybersecurity-related insights and information.

### 9. Global Intelligence
- Global digital threat information and visualisation.

### 10. Test Lab
- Environment for exploring and testing threat detection.

---

## 🧠 Artificial Intelligence & Machine Learning

ScamShield AI uses two complementary approaches:

**1. Rule-Based Threat Detection**

Identifies suspicious indicators such as:
- Urgency and pressure.
- Requests for sensitive information.
- Prize and reward claims.
- Suspicious link language.
- Impersonation.
- Credential requests.
- Threats and remote-access requests.

**2. Machine Learning SMS Classification**

The SMS classifier uses:
- TF-IDF Vectorization.
- Logistic Regression.
- SMS Spam Collection dataset.
- Spam probability estimation.

The model estimates whether an SMS resembles spam. It does not independently confirm financial fraud.

---

## 📊 Machine Learning Model Performance

The trained model was evaluated using a train-test split.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 98.30% |
| Precision | 93.92% |
| Recall | 93.29% |
| F1 Score | 93.60% |

These results represent performance on the evaluation split, not a guarantee of real-world detection accuracy.

---

## 📁 Dataset

**Dataset:** SMS Spam Collection

- Total messages: 5,572
- Legitimate messages (ham): 4,825
- Spam messages: 747

The dataset is stored locally in:

`data/SMSSpamCollection`

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- HTML
- CSS

---

## ⚙️ Installation & Setup

### Step 1: Clone or download the project

Download the ScamShield AI project folder to your computer.

### Step 2: Open the project directory

Open the project folder in Visual Studio Code.

### Step 3: Install dependencies

Open the VS Code terminal and run:

```bash
pip install -r requirement.txt
```

### Step 4: Run the application

```bash
python -m streamlit run app.py
```

### Step 5: Open the application

Visit:

`http://localhost:8501`

---

## 🔐 Privacy & Limitations

- Users manually submit information for analysis.
- The application does not automatically read SMS messages.
- It does not record or intercept phone calls.
- It does not access user contacts.
- Machine Learning predictions are estimates.
- Spam classification does not automatically mean fraud.
- Rule-based detection may produce false positives or miss unfamiliar scam patterns.
- Analysis is experimental and should not replace independent verification.

---

## 🎯 Project Objective

The primary objective of ScamShield AI is to make digital safety awareness more accessible by combining Artificial Intelligence, Machine Learning and cybersecurity education in one interactive platform.

The project aims to help users recognise suspicious digital communication and make more informed safety decisions.

---

## 👨‍💻 Project Information

**Project Name:** ScamShield AI  
**Project Type:** Artificial Intelligence Capstone Project  
**Application Type:** Web Application  
**Development Language:** Python  
**Framework:** Streamlit

---

*ScamShield AI — Think Before You Click. Stay Alert. Stay Protected.*
