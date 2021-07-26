# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:51:48 2021

@author: DELL
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    #print(integer_list)
    print(hash(integer_list))
