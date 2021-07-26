# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:54:19 2021

@author: DELL
"""


def count_substring(string, substring):
    cnt = 0
    for i in range(len(string) - len(substring) + 1): 
        if string[i:i+len(sub_string)] == substring:
            #print(string[i:i+len(sub_string)])
            cnt += 1
    return cnt

