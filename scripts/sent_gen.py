##prepare "sent" for training CRFs

import pickle
import os

train_sents_path='../data/txt_with_stresslabel/'
train_sents=[]
for efile in os.listdir(train_sents_path):
    content=open(train_sents_path+efile, 'r').read()
    words=content[2:-3].split('), (')
    train_sents_sub=[]
    for word in words:
        tmps=word.split(", ")
        labels=[]
        for tmp in tmps:
            tmp=tmp[1:-1]
            labels.append(tmp)
        train_sents_sub.append(labels)
    train_sents.append(train_sents_sub)
pickle.dump(train_sents,open('../data/train_sents.txt','wb'))