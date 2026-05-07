import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train(series):
    X,y=[],[]
    for i in range(len(series)-10):
        X.append(series[i:i+10])
        y.append(series[i+10])
    X,y=np.array(X),np.array(y)

    model=Sequential()
    model.add(LSTM(50,input_shape=(10,1)))
    model.add(Dense(1))
    model.compile(loss='mse',optimizer='adam')
    model.fit(X,y,epochs=3,verbose=0)
    return model

def predict(model,series):
    seq=np.array(series[-10:]).reshape(1,10,1)
    return model.predict(seq)[0][0]
