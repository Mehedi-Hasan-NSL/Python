# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:48:47 2021

@author: DELL
"""
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
#print(*sorted(input(), key=order.index), sep='')
input_str = input()
s = (sorted(input_str,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),''.join(x))))
#print(s)
print(*(s),sep = '')