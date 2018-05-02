import numpy as np
from numpy import linalg as la

def genTable(G,C):
    row = []
    for i in range(len(G)):
        column = []
        for j in range(len(C)):
            a = np.array(G[i])
            b = np.array(C[j])
            dist = la.norm(a-b)
            column.append(dist)
        row.append(column)
    return row

def DTW(table):
    dTable = []
    pTable = []
    for i in range(len(table)):
        columnD = []
        columnP = []
        for j in range(len(table[0])):
            columnD.append(100000)
            columnP.append([[i,j]])
        dTable.append(columnD)
        pTable.append(columnP)
    dTable[0][0] = table[0][0]
    for i in range(len(table)):
        for j in range(len(table[0])):
            a=1000000
            b=1000000
            c=1000000
            if j!=0:
                a = 1*table[i][j]+dTable[i][j-1]
            if i!=0:
                b = 0*table[i][j]+dTable[i-1][j]
            if (i!=0 and j!=0):
                c = 0*table[i][j]+dTable[i-1][j-1]
            if (i!=0 or j!=0):
                dTable[i][j] = min(a,b,c)
                if min(a,b,c) == c:
                    temp = pTable[i][j]
                    temp.extend(pTable[i-1][j-1])
                    pTable[i][j]=temp
                elif min(a,b,c) == a:
                    temp = pTable[i][j]
                    temp.extend(pTable[i][j-1])
                    pTable[i][j]=temp
                elif min(a,b,c) == b:
                    temp = pTable[i][j]
                    temp.extend(pTable[i-1][j])
                    pTable[i][j]=temp
    result = {'Path':pTable[len(table)-1][len(table[1])-1],'Value':dTable[len(table)-1][len(table[1])-1]}
    return result

def value(a,b):
    table = genTable(a,b)
    result = DTW(table)
    return result['Value']

def path(a,b):
    table = genTable(a,b)
    result = DTW(table)
    return result['Path']
