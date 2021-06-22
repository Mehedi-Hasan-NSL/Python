# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:19:07 2021

@author: DELL
"""

import numpy as np

row,col = map(int,input().split())

matA = np.array([input().split() for _ in range(row)],int)
#print(matA)
matB = np.array([input().split() for _ in range(row)],int)

print(matA+matB)
print(matA-matB)
print(matA*matB)
print(matA//matB)
print(matA%matB)
print(matA**matB)