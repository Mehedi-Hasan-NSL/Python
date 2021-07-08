# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:09:40 2021

@author: DELL
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def formingMagicSquare(square):

    minCost = 9 * 9
    for magicSquare in magicSquares:
        cost = 0
        
        for i in range(3):
            for j in range(3):
                #print(magicSquare[i][j])
                #print(square[i][j])
                cost += abs(magicSquare[i][j] - square[i][j])
        if cost < minCost:
            minCost = cost
    return minCost


square = [
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split()))
    ]


magicSquares = []
for a in range(1, 10):
    for b in range(1, 10):
        if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(range(1, 10)):
            magicSquares.append([[a, 15-a-b, b],
                                  [5+b-a, 5, 5+a-b],
                                  [10-b, a+b-5, 10-a]])
                                  
print(formingMagicSquare(square))