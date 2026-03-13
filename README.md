#  SentinelFlow – Transaction Risk Monitoring System

A **Streamlit-based web application** that monitors financial transactions and evaluates their **risk level** using rule-based analysis.

---

##  Features

* Real-time **transaction risk score (0–100%)**
* Visual **risk level indicator**: Low / Medium / High
* **Transaction summary table**
* **Fraud risk dashboard chart**
* **Transaction history viewer**

---

##  Project Structure

```
SentinelFlow/
│
├── app.py                # Main Streamlit application
├── analytics_det.ipynb   # Data analysis notebook
├── templates/
│   └── index.html        # Optional HTML template
├── .gitignore
└── README.md
```

---

## Setup & Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/Priyadharshinik15/SentinelFlow.git
cd SentinelFlow
```

---

###  Create a Conda Environment

```bash
conda create -n fraud_det python=3.10
conda activate fraud_det  
```

---

###  Install Dependencies

```bash
pip install 
scikit-learn==1.6.1
pandas
numpy
streamlit
joblib
```

---

##  Run the Application

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

##  How the System Works

The system evaluates transaction risk based on:

* Transaction amount
* Account balance changes
* Transaction type
* Transaction frequency



