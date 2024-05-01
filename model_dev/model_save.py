from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import OneHotEncoder

def round_to_half(num):
    num = num*2
    return round(num)/2

def RMSE(obs, pred):
    return ((obs-pred)**2).mean()**0.5

def MAE(obs, pred):
    return abs(obs-pred).mean()

print(sklearn.__version__)



data = pd.read_csv('model_dev/data/combined_data.csv',index_col=False)
with_bath = data[data['bathroom'].isna() == False]

bed_to_bath = {}
for i in sorted(with_bath['bedroom'].unique()):
    df=with_bath[with_bath['bedroom'] == i]
    bed_to_bath[i] = df['bathroom'].mean()

for k in bed_to_bath:
    bed_to_bath[k] = round_to_half(bed_to_bath[k])

bath_filled = data.copy()
def bath_fill(row):
    if np.isnan(row['bathroom']):
        row['bathroom'] = bed_to_bath[row['bedroom']]
    return row
bath_filled = bath_filled.apply(bath_fill,axis=1)

fin_data = bath_filled.drop(['address','type'],axis=1)
Y = fin_data['price']
X = fin_data.drop(['price'],axis=1)
city_enc = OneHotEncoder(handle_unknown='ignore')
city_enc.fit(fin_data[['city']])
print(city_enc.categories_)
city_coded = city_enc.transform(fin_data[['city']]).toarray()
for i,c in enumerate(city_enc.categories_[0]):
    X[c] = city_coded[:,i]
X = X.drop(['city'],axis=1)

model = RandomForestRegressor(max_depth = 9,criterion = 'friedman_mse')
model.fit(X ,Y)
pred = model.predict(X)
print(RMSE(pred, Y))
print(MAE(pred, Y))
dump(model, 'static/model/randomforest_9_friedman.joblib') 