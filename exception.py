# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:00:46 2021

@author: DELL
"""

n = int(input())
for i in range(n):
    try:  
        a,b = map(int,input().split()) 
        print(int(a)//(b))
    except Exception as e:
        print ("Error Code:",e)
    except ValueError as e:
        print ("Error Code:",e)