import joblib
import pandas as pd

# Load artifacts
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

def predict(input_dict):
    df = pd.DataFrame([input_dict])

    # Apply same preprocessing
    df = pd.get_dummies(df)
    df = df.reindex(columns=features, fill_value=0)

    prob = model.predict_proba(df)[:,1]
    pred = (prob > 0.5).astype(int)

    return {
        "prediction": int(pred[0]),
        "probability": float(prob[0])
    }