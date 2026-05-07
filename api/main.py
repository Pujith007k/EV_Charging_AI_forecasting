from fastapi import FastAPI
import pandas as pd
from models.lstm_model import train,predict

app=FastAPI()

@app.get("/predict")
def pred():
    df=pd.read_csv("data/ev_data.csv")
    s=df.ev_demand.values
    m=train(s.reshape(-1,1))
    p=predict(m,s)
    return {"prediction":float(p)}
