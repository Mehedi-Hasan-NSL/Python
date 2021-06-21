# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:44:53 2021

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    if re.match(r"^[7-9]\d{9}$",input()):       
        print("YES")
    else: print("NO")