# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:53:53 2021

@author: DELL
"""

#!/bin/python3

import math
import os
import random
import re
import sys



# write your code here
def avg(*nums):
    try:
        sum_nums = 0
        for num in nums:
            sum_nums += num
            
        return float(sum_nums/len(nums))
    except Exception as e:
        pass
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()