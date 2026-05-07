from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

@app.get("/predict")
def pred():
    if not os.path.exists("data/ev_data.csv"):
        from utils.data_generator import *
    
    df = pd.read_csv("data/ev_data.csv")
    return {"prediction": float(df.ev_demand.mean())}
