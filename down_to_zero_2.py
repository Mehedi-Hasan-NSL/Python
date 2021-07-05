# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:30:21 2021

@author: DELL
"""
import math
import numpy as np

def minMove(n):
    if (n <= 3): 
        return n;
    if (minMoves[n] > 0) :
        return minMoves[n];
    min1 = math.inf;
    for i in range(int(math.sqrt(n)),1,-1):
        if (n % i == 0) :
            factor = n//i;
            print(factor)
            min1 = min(min1, 1 + minMove(factor));
        
    
    min1 = min(min1, 1 + minMove(n-1));
    minMoves[n] = min1;
    return min1;

n = int(input())
minMoves = np.zeros(10**6)

print(minMove(n))