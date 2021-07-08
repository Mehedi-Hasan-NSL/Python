#!/bin/python3

import sys
#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:02:50 2021

@author: DELL
"""


def factorial( n) :
    res = [0]*1000

    res[0] = 1
    res_size = 1
    
    for i in range(2,n+1):
        res_size = multiply(i, res, res_size)
     
        
    for i in range(res_size-1,-1,-1):
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
    
         
def multiply(x, res,res_size) :
     
    carry = 0 
 
    """
    x= 10
    
    number = 124 
    
    4*10 + 0 = 40 carry 4 res 0
    2*10 + 4 = 24 carry 2 res 4
    1*10 + 2 = 12 carry 1 res 2
    
    carry 1 = res 1
    
    res = 1240
    
    """
    for i in range(res_size):
        temp = res[i] * x + carry
        carry = temp // 10
        res[i] = temp % 10

    while (carry) :
        res[res_size] = carry % 10
        carry = carry // 10
        res_size = res_size + 1
         
    return res_size
    
n = int(input().strip())
factorial(n)

