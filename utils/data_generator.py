import pandas as pd
import numpy as np

n=300
df=pd.DataFrame({
"time":pd.date_range("2025-01-01",periods=n,freq="H"),
"lat":np.random.uniform(12.9,13.1,n),
"lon":np.random.uniform(77.5,77.7,n),
"ev_demand":np.random.randint(10,120,n),
"grid_load":np.random.randint(50,150,n)
})

df.to_csv("data/ev_data.csv",index=False)
print("data generated")
