# 🏥 Predicting In-Hospital Mortality Using Clinical Data

## 📌 Overview

This project aims to predict the likelihood of in-hospital mortality for surgical patients using clinical and operational data from the PhysioNet INSPIRE dataset.

The goal is to assist healthcare providers in identifying high-risk patients early and improving clinical decision-making.

---

## 📊 Dataset

* Source: PhysioNet (INSPIRE dataset)
* Contains patient demographics, surgery timings, anesthesia data, and hospital stay information

---

## 🎯 Problem Statement

Can we predict whether a patient will experience in-hospital mortality based on pre-operative and intra-operative data?

---

## 🧹 Data Preprocessing

* Dropped columns with >80% missing values
* Imputed missing values:

  * Median for skewed numerical features
  * Mode for ordinal features (ASA score)
* Outlier handling using IQR-based winsorization
* Filtered dataset to include only first admissions per patient

---

## ⚙️ Feature Engineering

Key engineered features include:

* Surgery duration
* Anesthesia duration
* Pre-operative waiting time
* Post-operative hospital stay
* Body Mass Index (BMI)
* Risk categorization based on ASA score

---

## 🤖 Modeling

Models used:

* Logistic Regression
* Random Forest

Evaluation metrics:

* Accuracy
* Precision, Recall
* ROC-AUC Score

---

## 📈 Results

* Random Forest achieved the best performance
* Key predictors:

  * ASA score
  * Age
  * Surgery duration
  * Pre-operative wait time

---

## 🔍 Insights

* Higher ASA scores strongly correlate with mortality risk
* Longer hospital stays before surgery increase risk
* Extended surgery duration is associated with worse outcomes

---

## 🚀 Future Work

* Incorporate more clinical features
* Use advanced models like XGBoost
* Deploy as a clinical decision support tool

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* Matplotlib / Seaborn
* Jupyter Notebook

---

## 📌 Author

[Your Name]
