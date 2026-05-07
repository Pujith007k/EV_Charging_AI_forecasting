from fastapi import FastAPI
import pandas as pd
import os
import numpy as np

app = FastAPI()

def generate_data():
    import pandas as pd
    import numpy as np

    n = 200
    df = pd.DataFrame({
        "time": pd.date_range("2025-01-01", periods=n, freq="H"),
        "ev_demand": np.random.randint(10, 120, n),
        "grid_load": np.random.randint(50, 150, n)
    })

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/ev_data.csv", index=False)


@app.get("/predict")
def predict():
    # ✅ Auto-create data if missing
    if not os.path.exists("data/ev_data.csv"):
        generate_data()

    df = pd.read_csv("data/ev_data.csv")

    # ✅ Simple fast prediction (stable)
    prediction = np.mean(df["ev_demand"].tail(10))

    return {"prediction": float(prediction)}
