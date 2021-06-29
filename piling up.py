# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:15:39 2021

@author: DELL
"""
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    
    print(min_list)
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")

from time import time
from collections import deque
t0 = time()
for _ in range(int(input())):  
    _, queue =input(), deque(map(int, input().split()))
    
    for cube in reversed(sorted(queue)):
        print(cube)
        if queue[-1] == cube: queue.pop()
        elif queue[0] == cube: queue.popleft()
        else:
            print('No')
            break
    else: print('Yes')
    
print('Elapsed time :', time() - t0 )