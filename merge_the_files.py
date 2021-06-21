# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:21:09 2021

@author: DELL
"""

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        t = string[i:i+k]
        temp = ""
        for a in t:
            if a not in temp:
                temp += a
        print(temp)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
