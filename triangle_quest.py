# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:03:41 2021

@author: DELL
"""
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*(10**(i-1)) + (i*(10**(i-1)))//9)
