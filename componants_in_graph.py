# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:55:25 2021

@author: DELL
"""

def makeset(n):
    par[n]=n

def find(r):
    if par[r]==r: 
        return r
    par[r] = find(par[r])
    return par[r]   
def union(a,b):
    u=find(a)
    v=find(b)
    if u > v: 
        par[v]= u #Or you can write par[v]=u too
        count[u] += count[v]
        count[v] = 0 
    else :
        par[u] = v
        count[v] += count[u]
        count[u] = 0
        
edges = list([])
n = int(input())
par=[None]*(2*n+1) 
count = [1 for i in range(2*n+1)]
for i in range(1,2*n+1):
    makeset(i)
         
for i in range(n):
    a,b = map(int,input().split())
    edges.append([a,b])

    union(a,b)
    #(par)
    #print("  ",count)
        
mincount = min(filter(lambda x : x > 1 ,count))
maxcount = max(count)
print(mincount, maxcount)