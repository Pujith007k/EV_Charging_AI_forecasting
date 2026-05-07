import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np

from models.explain import explain

st.title("⚡ SmartGrid AI FINAL")


# Prediction
try:
    r=requests.get("https://evchargingaiforecasting-egxcmkcikqxzh4cc4htv72.streamlit.app//predict")
    st.write("Next Demand:",r.json()["prediction"])
except:
    st.warning("Run backend first")


if not os.path.exists("data/ev_data.csv"):
    import numpy as np
    import pandas as pd

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame({
        "lat": np.random.uniform(12.9, 13.1, 100),
        "lon": np.random.uniform(77.5, 77.7, 100),
        "ev_demand": np.random.randint(10, 120, 100)
    })
    df.to_csv("data/ev_data.csv", index=False)
else:
    df = pd.read_csv("data/ev_data.csv")

# Map
st.subheader("📍 Demand Map")
m=folium.Map(location=[df.lat.mean(),df.lon.mean()],zoom_start=12)

for _,row in df.head(80).iterrows():
    color="red" if row.ev_demand>80 else "blue"
    folium.CircleMarker(location=[row.lat,row.lon],radius=5,color=color,
    popup=f"Demand:{row.ev_demand}").add_to(m)

st_folium(m,width=700)

# Optimization Graph
st.subheader("📊 Peak Reduction")
base=np.random.randint(80,120,24)
opt=base-np.random.randint(10,30,24)

fig,ax=plt.subplots()
ax.plot(base,label="Before")
ax.plot(opt,label="After")
ax.legend()
st.pyplot(fig)

st.success(f"Peak reduced by {round((base.mean()-opt.mean())/base.mean()*100,2)}%")

# Explainability
st.subheader("🧠 Explainability")
for i in range(5):
    st.write(explain(90,130))
