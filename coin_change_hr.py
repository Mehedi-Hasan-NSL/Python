# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:54:50 2021

@author: DELL
"""

def cc(w):
    if w < 0 : return -1
    if w == 0 : return 0
    if mem[w] != 0 :
        return mem[w]
    
    for i in range(m):
        #ans = min(ans,1+cc(w - coins[i]))   
        print("coin",coins[i])
        print("return",cc(w - coins[i]),"w",w)
        ans = 1+ cc(w - coins[i])
        print("coin",coins[i],"ans",ans)
        
    #print("w ", w,"coin",coins[i])    
    mem[w] = ans
    print(mem)
    return mem[w] 
   
# n = weight m = len(coins)

n, m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [1]+[0]*n
mem = [1]+[0]*(n)
ans= 0
cc(n)
print(mem)
for i in range(m): 
    for j in range(coins[i], n+1): 
        #print(dp[j-coins[i]])
        dp[j]+=dp[j-coins[i]]
        #print(dp)

print(dp[n])