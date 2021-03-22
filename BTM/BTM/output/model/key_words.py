import numpy as np
x=[]
with open('../voca.txt','r')as f:
    for row in f.readlines():
        x.append(row.split()[1])

y=[]
with open('k20.pw_z','r')as f:
    rows=f.readlines()
    for row in rows:
        y.append(row.split())

with open('res.txt','w',encoding='utf-8')as f:
    for i in y:
        yi=np.argsort(i)[:20]
        s=' '.join([x[j] for j in yi])
        f.write(s+'\n')