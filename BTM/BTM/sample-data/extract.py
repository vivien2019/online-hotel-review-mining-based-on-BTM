import jieba
import jieba.analyse
import jieba.posseg

import pandas as pd

stopwords = [line.strip() for line in open('tingyongci.txt',encoding='UTF-8').readlines()]
f=open('review2.txt','w',encoding='utf-8')

df=pd.read_csv('wenben.csv')
for row in df['review']:
    sentence_depart = jieba.posseg.cut(row.strip())
    outs=[]

    for word,flag in sentence_depart:
        if flag=='n':
            print(word)
            outs.append(word)

    if len(outs)>0:
        f.write(' '.join(outs)+'\n')
    else:
        print(row)

f.close()
"""
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outs.append(word)
"""
