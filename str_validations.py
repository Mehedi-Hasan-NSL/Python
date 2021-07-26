# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:54:43 2021

@author: DELL
"""

s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
