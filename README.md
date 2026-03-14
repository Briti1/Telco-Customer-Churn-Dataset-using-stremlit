# Telco Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn is a major problem for telecom companies because acquiring new customers is more expensive than retaining existing ones.

This project builds a **Machine Learning model to predict whether a customer will churn (leave the service) or stay** based on various customer attributes such as tenure, contract type, internet service, payment method, and monthly charges.

The model is trained using the **Telco Customer Churn dataset** and deployed as an interactive web application using **Streamlit**, allowing users to input customer details and instantly predict churn probability.

---

## Problem Statement

Telecom companies face high customer attrition. Identifying customers who are likely to churn can help companies take preventive actions such as offering promotions or improving customer service.

The goal of this project is to:

* Analyze customer behavior using **Exploratory Data Analysis (EDA)**
* Build a **Machine Learning classification model**
* Deploy the model through a **Streamlit web application**

---

## Dataset

The dataset used in this project is the **Telco Customer Churn Dataset**, which contains information about telecom customers.

### Key Features

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* PhoneService
* MultipleLines
* InternetService
* OnlineSecurity
* OnlineBackup
* DeviceProtection
* TechSupport
* StreamingTV
* StreamingMovies
* Contract
* PaperlessBilling
* PaymentMethod
* MonthlyCharges
* TotalCharges

### Target Variable

* **Churn**

  * Yes → Customer leaves
  * No → Customer stays

---

## Project Workflow

### 1. Data Preprocessing

* Removed unnecessary columns
* Handled missing values
* Converted categorical variables
* Applied **One-Hot Encoding**

### 2. Exploratory Data Analysis (EDA)

EDA was performed to understand patterns in customer behavior.

Key visualizations include:

* Customer churn distribution
* Contract vs churn analysis
* Internet service usage
* Correlation matrix
* Monthly charges distribution

---

### 3. Model Building

The following machine learning algorithm was used:

* Random Forest Classifier

Steps performed:

* Train-Test Split
* Feature Scaling using StandardScaler
* Model Training
* Model Evaluation

---

### 4. Model Deployment

The trained model was deployed using **Streamlit** to create an interactive web application.

Users can input customer information and receive:

* Churn prediction
* Probability score

---

## Tech Stack

Programming Language:

* Python

Libraries Used:

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* streamlit
* pickle

---

## Project Structure

```
Telco-Customer-Churn-Prediction
│
├── data
│   └── Telco-Customer-Churn.csv
│
├── model
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── notebooks
│   └── model_building.ipynb
│
├── app.py
│
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/telco-churn-prediction.git
```

### 2. Navigate to the project folder

```
cd telco-churn-prediction
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```
streamlit run app.py
```

The application will open in your browser.

---

## Streamlit Application Features

* User-friendly interface
* Customer data input form
* Real-time churn prediction
* Probability score display

---

## Model Evaluation

The Random Forest model provides good performance for classification problems with mixed categorical and numerical features.

Evaluation metrics considered:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Future Improvements

Possible improvements for this project include:

* Hyperparameter tuning
* Trying additional algorithms such as XGBoost or LightGBM
* Adding more interactive visualizations
* Deploying the application on cloud platforms
* Adding model explainability using SHAP

---

## Learning Outcomes

Through this project I learned:

* Data preprocessing and cleaning
* Exploratory Data Analysis
* Feature engineering
* Machine learning model training
* Model deployment using Streamlit
* Building end-to-end ML projects


This project is open source and available under the MIT License.
