# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:32:27 2021

@author: DELL
"""
a = [1, 2, 3, 4, 5]
print(a)
print(x for x in a) 

from itertools import groupby
ans = []
for k,c in groupby(input()):
    ans.append((len(list(c)), int(k)))
#print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

print(*ans)
