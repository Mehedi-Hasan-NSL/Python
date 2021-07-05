# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:32:53 2021

@author: DELL
"""

element=5
par=[None]*(element+1) #Creating an array with 6 elements


def makeset(n):
    par[n]=n

for i in range(1,element+1):
    makeset(i)
    
def find(r):
    if par[r]==r: return r
    par[r] = find(par[r])
    return par[r]   

def union(a,b):
    u=find(a)
    v=find(b)
    if u==v: 
        print ("They are already friends")
    else: 
        par[u]=v #Or you can write par[v]=u too
        
print(find(1))

union(1,2)
union(2,3)

print(find(1))
