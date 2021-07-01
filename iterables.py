# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:07:03 2021

@author: DELL
"""

from itertools import combinations

_,s,n = input(),input().split(),int(input())
c = list(combinations(s,n))
f = list(filter(lambda x: 'a' in x, c))
print(len(f)/len(c))