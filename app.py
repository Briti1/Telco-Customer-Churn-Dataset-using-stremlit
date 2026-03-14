import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("D:\Projects\Machine Learning\Telco Customer Churn Dataset using stremlit\Telco-Customer-Churn-Dataset-using-stremlit\model\churn_model.pkl", "rb"))
scaler = pickle.load(open("D:\Projects\Machine Learning\Telco Customer Churn Dataset using stremlit\Telco-Customer-Churn-Dataset-using-stremlit\model\scaler.pkl", "rb"))
feature_columns = pickle.load(open(r"D:\Projects\Machine Learning\Telco Customer Churn Dataset using stremlit\Telco-Customer-Churn-Dataset-using-stremlit\model\feature_columns.pkl","rb"))
st.title("Telco Customer Churn Prediction")

st.write("Enter customer details to predict churn.")

# Taking User Inputs.

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["Yes","No"])
Partner = st.selectbox("Partner", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["Yes","No"])
tenure = st.slider("Tenure (Months)", 0, 72)

PhoneService = st.selectbox("Phone Service", ["Yes","No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes","No"])

InternetService = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])

OnlineSecurity = st.selectbox("Online Security", ["Yes","No"])
OnlineBackup = st.selectbox("Online Backup", ["Yes","No"])
DeviceProtection = st.selectbox("Device Protection", ["Yes","No"])
TechSupport = st.selectbox("Tech Support", ["Yes","No"])

StreamingTV = st.selectbox("Streaming TV", ["Yes","No"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes","No"])

Contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes","No"])

PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"]
)

MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

# Convert Inputs to DataFrame 

input_dict = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

#Input DataFrame Created

input_df = pd.DataFrame([input_dict])  

# Encoding Categorical data for predicting

binary_cols = [
    "gender","Partner","Dependents","PhoneService","MultipleLines",
    "OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
    "StreamingTV","StreamingMovies","PaperlessBilling"
]

for col in binary_cols:
    input_df[col] = input_df[col].map({"Yes":1,"No":0,"Male":1,"Female":0})


# Apply same one-hot encoding for multi-category values
input_df = pd.get_dummies(input_df)

# Align columns with training data
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Scale features using standard scaler

input_scaled = scaler.transform(input_df)

# Predicting the output with probability

if st.button("Predict Churn"):

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"Customer is likely to CHURN ⚠️  (Probability: {probability:.2f})")
    else:
        st.success(f"Customer will STAY ✅ (Probability: {1-probability:.2f})")