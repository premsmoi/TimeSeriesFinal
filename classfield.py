import DTW as dtw
import pandas as pd
import numpy as np
import random
import ED as ed

train_file = "SwedishLeaf_TRAIN.csv"

df1 = pd.read_csv(train_file, header=None)
acc = []
for r in range(1):
    #df1 = df1.sample(frac=1).reset_index(drop=True)

    n_train = int(len(df1)*4/5)
    
    all_label = np.array(df1.iloc[:,0:1].copy())
    all_data = np.array(df1.iloc[:,1:145].copy())

    '''
    test_label = all_label[n_train+1:len(df1)]
    test_data = all_data[n_train+1:len(df1)]

    train_label = all_label[0:n_train+1]
    train_data = all_data[0:n_train+1]

    '''

    test_label = all_label[400:500]
    test_data = all_data[400:500]

    train_label = all_label[0:400]
    train_data = all_data[0:400]

    classifield_label = []
    for i in range(len(test_data)):
        minDistance = 10000
        label = 0
        for j in range(len(train_data)):
            dis = dtw.value(test_data[i],train_data[j])
            #dis = ed.value(test_data[i],train_data[j])
            if dis < minDistance:
                label = train_label[j]
                minDistance = dis
        print("data "+str(i+1)+" is "+str(label))
        print("data "+str(i+1)+" truly is "+str(test_label[i]))
        classifield_label.append(label)     
    #print(classifield_label)
    same = 0
    for i in range(len(test_label)):
        if test_label[i]==classifield_label[i]:
            same = same+1
    accI = 1.0*same/len(test_label)
    acc.append(accI)
    print(accI)
    
print(acc)
print(np.mean(acc))
