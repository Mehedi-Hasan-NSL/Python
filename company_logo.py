# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:22:24 2021

@author: DELL
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    cnt = {}
    for a in s:
        if a not in cnt:
            cnt[a] = 1
        else:
             cnt[a] += 1
    #print(cnt.items())
    
    s_sorted = sorted(sorted(cnt.items()),key = lambda x : x[1],reverse = True)
    #print(s_sorted)
    top_3 = s_sorted[:3]
    #print(top_3)
    for k in range(3):
        print(s_sorted[k][0],s_sorted[k][1])