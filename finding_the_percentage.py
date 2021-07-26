# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:50:16 2021

@author: DELL
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    nums = student_marks[query_name]
    print("{0:.2f}".format(sum(nums)/ len(nums)))
    #print(round(sum(nums)/ len(nums)))