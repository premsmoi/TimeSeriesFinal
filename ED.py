import numpy as np

def value(a,b):
    sum = 0
    for i in range(len(a)):
        sum = sum+((a[i]-b[i])**2)
        
    sum = sum**0.5
    
    return sum
