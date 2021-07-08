# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 17:06:09 2021

@author: DELL
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    # Write your code here
    if n == 0 : return t1 
    if n == 1 : return t2
    if mem[n] != -1 : return mem[n]

    mem[n] = fibonacciModified(t1,t2,n-1)**(2) + fibonacciModified(t1,t2,n-2)  
    
    return mem[n]
    
    
fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

t1 = int(first_multiple_input[0])

t2 = int(first_multiple_input[1])

n = int(first_multiple_input[2])

mem = [-1]*(n+1)
result = fibonacciModified(t1, t2, n)

fptr.write(str(mem[n-1]) + '\n')

fptr.close()
