# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:30:26 2021

@author: DELL
"""

from fractions import Fraction
from functools import reduce
from fractions import gcd
def product(fracs):
    t = reduce(lambda x,y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
        #print(*fracs)
    result = product(fracs)
    print(*result)
    

n = int(input())
rationals = []
for i in range(n):
    rationals.append(list(map(int, input().split())))
s = [list(a) for a in zip(*rationals)]
print(s)
k = [reduce(lambda x, y: x*y, s[i]) for i in range(2)]
c = reduce(gcd, k)
for i in range(2):
    k[i] //= c
print(*k)