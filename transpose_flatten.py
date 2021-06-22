# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:06:56 2021

@author: DELL
"""

import numpy as np

row , col = map(int , input().split())
my_array=[]
for i in range(row) :
    a = input().split()
    my_array.append(np.array(a,int))
    #print(my_array)
my_array = np.array(my_array,np.int32)

print(my_array.T)
print(my_array.flatten())