#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import pickle
from tensorflow.keras.models import load_model
import joblib
model_1 = joblib.load('flu/flu_DecisionTreeClassifier.sav')
model_2 = load_model('flu/mlp')
model_3 = joblib.load('flu/flu_KNeighborClassifier.sav')
model_4 = joblib.load('covid-19/covid_DecisionTreeRegression.sav')
model_5 = load_model('covid-19/mlp')
model_6 = joblib.load('covid-19/covid_KNeighborRegressor.sav')
model_7 = joblib.load('flu-trend/flu_DecisionTreeRegression.sav')
model_8 = joblib.load('flu-trend/flu_KNeighborRegressor.sav')

#from tensorflow.keras.layers import Dense,BatchNormalization
#from tensorflow.keras import layers
#from tensorflow import keras
#import numpy as np
#from sklearn.metrics import r2_score
#from tensorflow.keras.layers.experimental import preprocessing
#from tensorflow.keras.callbacks import EarlyStopping
#from scipy import stats


# In[2]:


s = socket.socket()
name = '192.168.1.189'
host = socket.gethostbyname(name)
port = 8080
s.bind((host,port))
s.listen(10)
print('server_start')
while True:
    conn, addr = s.accept()
    print(addr, "Has connected to the server")
    #receive data
    received_data  = conn.recv(519168)
    received_data  = pickle.loads(received_data)
    #procession flu
    if received_data[0] == "flu":
        del received_data[0]
        for i in range(len(received_data)):
            received_data[i] = int(received_data[i])
        received_data = [received_data]
        print(received_data )
        result1 = model_1.predict(received_data)
        result2 = model_2.predict_classes(received_data)
        result3 = model_3.predict(received_data )
        y = result1[0] + result2[0] + result3[0]
        if y == 0:
            y = "Based on data and model, you needn't take flu shot"
        elif y ==1:
            y = "Based on data and model, suggest you take flu shot"
        elif y ==2:
            y = "Based on data and model, strongly suggest you take flu shot"
        else:
            y = "Based on data and model, very strongly suggest you take flu shot"
    #procssion Covid
    elif received_data[0] == "covid":
        del received_data[0]
        for i in range(len(received_data)):
            received_data[i] = int(received_data[i])
        received_data = [received_data]
        print(received_data)
        result1 = model_4.predict(received_data)
        result2 = model_5.predict_classes(received_data)
        result3 = model_6.predict(received_data)
        y = result1[0] + result2[0] + result3[0]
        y = int(int(y[0])/3)
        y = "Based on data and model, today, there should be {} new covid cases. Stay safe!".format(y)
    else:
        del received_data[0]
        for i in range(len(received_data)):
            received_data[i] = int(received_data[i])
        received_data = [received_data]
        result1 = model_7.predict(received_data)
        result2 = model_8.predict(received_data)
        y = result1[0] + result2[0]
        print(y)
        y = int(y/2)
        y = "Based on data and model, today, there should be {} new flu cases. Stay safe!".format(y)
    print(y)
        
    print("Data has been calculated successfully")
    # send data
    data = pickle.dumps(y)
    conn.send(data)
    print("Data has been sent successfully")


# In[ ]:




