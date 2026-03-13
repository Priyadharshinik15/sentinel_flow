import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("fraud_detection_pipeline.pkl")

# Title
st.title("💳 Transaction Risk Monitoring System")

st.markdown("### Please enter the transaction details")
st.divider()

# Transaction inputs
transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

amount = st.number_input("Transaction Amount", min_value=0.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0)

newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0)

newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0)


# Create history storage
if "history" not in st.session_state:
    st.session_state.history = []


# Predict button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # 1️⃣ Fraud Risk Score
    st.subheader("Risk Score")
    st.write(round(probability*100,2), "%")
    st.progress(float(probability))


    # 2️⃣ Risk Level Indicator
    if probability < 0.3:
        st.success("Low Risk Transaction")
    elif probability < 0.7:
        st.warning("Medium Risk Transaction")
    else:
        st.error("High Risk Transaction")


    # 3️⃣ Transaction Summary Table
    st.subheader("Transaction Summary")
    st.dataframe(input_data)


    # Store history
    input_data["RiskScore"] = probability
    input_data["Prediction"] = prediction
    st.session_state.history.append(input_data)


# 4️⃣ Fraud Dashboard Chart
st.subheader("Risk Dashboard")

if st.session_state.history:
    history_df = pd.concat(st.session_state.history)

    chart_data = history_df["Prediction"].value_counts()
    st.bar_chart(chart_data)


# 5️⃣ Transaction History
st.subheader("Transaction History")

if st.session_state.history:
    history_df = pd.concat(st.session_state.history)
    st.dataframe(history_df)
# import streamlit as st
# import pandas as pd
# import joblib

# # Load trained pipeline
# model = joblib.load("fraud_detection_pipeline.pkl")

# # Title
# st.title("💳 Fraud Detection Prediction App")

# st.markdown("### Please enter the transaction details")
# st.divider()

# # Transaction inputs
# transaction_type = st.selectbox(
#     "Transaction Type",
#     ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
# )

# amount = st.number_input("Transaction Amount", min_value=0.0)

# oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0)

# newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0)

# oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0)

# newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0)
# if st.button("Predict"):

#     input_data = pd.DataFrame({
#         "type": [transaction_type],
#         "amount": [amount],
#         "oldbalanceOrg": [oldbalanceOrg],
#         "newbalanceOrig": [newbalanceOrig],
#         "oldbalanceDest": [oldbalanceDest],
#         "newbalanceDest": [newbalanceDest]
#     })

#     prediction = model.predict(input_data)[0]
#     probability = model.predict_proba(input_data)[0][1]

#     st.subheader(f"Prediction : '{prediction}'")
#     st.write(f"Fraud Probability : {probability:.2f}")

#     if prediction == 1:
#         st.error("⚠️ This transaction looks like it is a FRAUD!")
#     else:
#         st.success("This transaction looks like it is not a fraud")