# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:49:11 2021

@author: DELL
"""

d={} #1
for _ in range(int(input())): #2
    Name= input() #3
    Grade=float(input()) #4
    d[Name]=Grade #5

sorted_d = sorted(d.items(), key = lambda x : x[1], reverse = True)

sec = sorted_d[-2][1]
v=d.values()#6
second=sorted(list(set(v)))[1] #7
second_lowest=[] #8
for key,value in d.items():  #9
    if value==second: #10
        second_lowest.append(key) #11
second_lowest.sort() #12
for name in second_lowest: #13
    print (name) #14
