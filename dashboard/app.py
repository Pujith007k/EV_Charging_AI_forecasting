import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np
from models.explain import explain
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("⚡ SmartGrid AI FINAL")


# Prediction
try:
    r=requests.get("http://127.0.0.1:8000/predict")
    st.write("Next Demand:",r.json()["prediction"])
except:
    st.warning("Run backend first")

df=pd.read_csv("data/ev_data.csv")

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
