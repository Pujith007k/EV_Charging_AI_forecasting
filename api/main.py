from fastapi import FastAPI
import pandas as pd
import os
import numpy as np

app = FastAPI()

@app.get("/predict")
def pred():
    if not os.path.exists("data/ev_data.csv"):
        from utils.data_generator import *
    
    df = pd.read_csv("data/ev_data.csv")

    # Simple prediction (fast + stable)
    prediction = np.mean(df["ev_demand"].tail(10))

    return {"prediction": float(prediction)}
