# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:38:29 2021

@author: DELL
"""

"""
The trick to this challenge is to realize that there are n+(n-1)+(n-2)+...+2+1=n(n+1)/2 
substrings in a word of length n. 
Therefore, since any substring starts exclusively with 
either a vowel or a consonant, we only need to count the number 
of substrings starting with a vowel and subtract from the total 
number of substrings to get the number of substrings starting with a consonant, or vice versa.

"""


def minion_game(s):
    s1 = 0
    s2 = 0
    for i in range(len(s)):
        if s[i] not in 'AEIOU':
            #s1 += len(s[i:])
            s1 += len(s) - i
        else:
            s2 += len(s) - i
    if s1 > s2:
        print("Stuart", s1)
    elif s2 > s1:
        print("Kevin", s2)
    else:
        print("Draw")


minion_game(input())
