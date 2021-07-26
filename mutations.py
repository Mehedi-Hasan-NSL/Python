# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:53:40 2021

@author: DELL
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return string[:position] + character + string[position+1:]
    #return ''.join(l)