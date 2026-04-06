from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

# Define input schema
class Patient(BaseModel):
    age: float
    asa: int
    bmi: float
    emop: int
    surgery_duration: float
    anesthesia_duration: float
    preop_wait_time: float

@app.get("/")
def home():
    return {"message": "Mortality Prediction API"}

@app.post("/predict")
def predict_patient(data: Patient):
    result = predict(data.dict())
    return result