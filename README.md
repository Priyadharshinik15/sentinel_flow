

**SentinelFlow** is a machine learning–based transaction risk monitoring system designed to detect potentially fraudulent financial transactions. The system analyzes key transaction attributes such as transaction type, amount, and account balances to estimate the likelihood of fraud. A trained machine learning pipeline processes the input data and generates a risk score that classifies transactions into low, medium, or high risk. The predictions and transaction insights are presented through an interactive dashboard built using Streamlit, allowing users to monitor and analyze transaction risks in real time.

---

##  Features

* Real-time **transaction risk score (0–100%)**
* Visual **risk level indicator**: Low / Medium / High
* **Transaction summary table**
* **Fraud risk dashboard chart**
* **Transaction history viewer**


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
These factors are used to calculate a risk score and classify transactions into:

🟢 Low Risk

🟡 Medium Risk

🔴 High Risk


