import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Approval Prediction App")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Amount Term (in days)", value=360.0)
credit_history = st.selectbox("Credit History", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Encode user input
def encode_input():
    return [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        1.0 if credit_history == "Yes" else 0.0,
        {"Urban": 2, "Rural": 0, "Semiurban": 1}[property_area]
    ]

if st.button("Predict Loan Approval"):
    input_data = np.array([encode_input()])
    prediction = model.predict(input_data)[0]
    st.success("✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected")
