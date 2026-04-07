# 🏥 Predicting In-Hospital Mortality Using Clinical Data

## 📌 Overview

This project aims to predict the likelihood of **in-hospital mortality for surgical patients** using clinical and operational data from the PhysioNet INSPIRE dataset.

The objective is to assist healthcare providers in identifying high-risk patients early and improving clinical decision-making.

---

## 🎯 Problem Statement

Can we accurately predict whether a patient will experience in-hospital mortality using pre-operative and intra-operative data?

---

## 📊 Dataset

* Source: PhysioNet (INSPIRE dataset)
* Includes:

  * Patient demographics (age, sex, BMI)
  * Clinical indicators (ASA score)
  * Surgery and anesthesia timings
  * Hospital operational data

---

## 🧹 Data Preprocessing

* Dropped columns with >80% missing values
* Removed non-informative columns (e.g., constant features)
* Handled missing values:

  * Median imputation for skewed numerical features
  * Mode imputation for ordinal features (ASA)
* Outlier handling using IQR-based winsorization
* Converted time-based features to numeric values (seconds)
* Filtered dataset to include only one encounter per patient

---

## ⚙️ Feature Engineering

Key engineered features:

* Surgery duration
* Anesthesia duration
* Pre-operative waiting time
* Body Mass Index (BMI)
* Risk indicator (ASA-based)
* Interaction feature: `ASA × surgery duration`

---

## 🚨 Handling Class Imbalance

The dataset is highly imbalanced (~1% mortality rate).

Techniques used:

* Class weighting
* Threshold tuning
* SMOTE (Synthetic Minority Oversampling Technique)

---

## 🤖 Models Trained

| Model                       | Notes                                 |
| --------------------------- | ------------------------------------- |
| Logistic Regression         | Baseline model                        |
| Logistic Regression + SMOTE | Best performing                       |
| Random Forest               | Compared for non-linearity            |
| XGBoost                     | Used for performance + explainability |

---

## 📈 Results

### ✅ Final Model: Logistic Regression + SMOTE

* Recall (mortality): **0.83**
* Precision (mortality): **0.06**
* ROC-AUC: **~0.87**

👉 High recall ensures most high-risk patients are identified.

---

## 🔍 Model Explainability (SHAP)

SHAP analysis revealed key drivers of mortality:

* Emergency operations (strongest predictor)
* ASA score (patient condition)
* Surgery duration (complexity)
* Age

### Key Insight:

> Mortality risk is driven by a combination of patient condition and surgical complexity.

---

## 🧠 Key Insights

* Higher ASA scores significantly increase mortality risk
* Emergency surgeries are strongly associated with poor outcomes
* Longer and more complex procedures increase risk
* Feature interactions (ASA × duration) improve predictive power

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* Scikit-learn
* XGBoost
* SHAP
* Matplotlib / Seaborn

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

```bash
python src.api:app
```


