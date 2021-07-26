# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:51:02 2021

@author: DELL
"""

lis=[]
for _ in range(int(input())):
    command, *value = input().split()
    if command == 'print':
        print(lis)
    else:
        getattr(lis,command)(*(map(int, value)))    #lis.insert()/lis.pop() .....