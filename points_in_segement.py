# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:46:52 2021

@author: DELL
"""

def low(array, key):
    begin=0
    end=len(array)-1
    index=None
    while begin<=end:
        mid=(begin+end)//2
        if key == array[mid]:
            index=mid #The value is found, save the index.
            end = mid - 1 
            #begin = mid + 1 
            
        elif key > array[mid]: begin=mid+1 #Search the right portion
        elif key < array[mid]: end=mid-1 #Search the left portion
    return end #If the number is not found, index will contain None.

def high(array, key):
    begin=0
    end=len(array)-1
    index=None
    while begin<=end:
        mid=(begin+end)//2
        if key == array[mid]:
            index=mid #The value is found, save the index.
            #end = mid - 1 
            begin = mid + 1 
            
        elif key > array[mid]: begin=mid+1 #Search the right portion
        elif key < array[mid]: end=mid-1 #Search the left portion
    return end #

#info=list(map(int,input().split()))
#info=[100,2,10,50,20,500,150,200,1000]
#print(info1)

#print(info)
for _ in range(int(input())):
    n,q = map(int,input().split())
    
    info=list(map(int,input().split()))
    for _ in range(q):
        l,h = map(int,input().split())
        #info=sorted(info)
        print("",high(info,h)-low(info,l))
        #print (search(info,key))