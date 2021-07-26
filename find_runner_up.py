# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:48:07 2021

@author: DELL
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(max([a for a in arr if a != max(arr)]))
