# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:52:09 2021

@author: DELL
"""

def swap_case(s):
    return ''.join(i.lower() if i.isupper() else i.upper() for i in s)