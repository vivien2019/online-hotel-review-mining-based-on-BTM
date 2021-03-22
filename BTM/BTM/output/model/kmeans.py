import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

with open('k10.pw_z','r')as f:
    rows=f.readlines()

df=pd.DataFrame([row.strip().split(' ') for row in rows])
X=df.T
y_pred = KMeans(n_clusters=20, random_state=9).fit_predict(X)

d={}
for i in range(len(y_pred)):
    p=y_pred[i]
    if p in d:
        d[p].append(i)
    else:
        d[p]=[i]