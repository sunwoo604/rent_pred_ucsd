from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import sklearn
import os

print(sklearn.__version__)
print(os.getcwd())

model = RandomForestRegressor(max_depth = 9,criterion = 'friedman_mse')
model = load(os.getcwd()+'/static/model/randomforest_9_friedman.joblib')
cities = ['Bay Ho', 'Clairemont Mesa East', 'Clairemont Mesa West',
       'Del Mar Heights', 'Kearny Mesa', 'La Jolla', 'Linda Vista',
       'Mira Mesa', 'North Clairemont', 'Pacific Beach',
       'Sorrento Valley', 'University City']

def pred_rent(bed, bath, city):
    x = featurization(bed,bath,city)
    pred = model.predict(x)
    return round(pred[0],-1)

def featurization(bed,bath,city):
    out = [bed,bath]
    for i in cities:
        if city == cities:
            out += [1]
        else:
            out += [0]
    return [out]