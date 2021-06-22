# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:01:54 2021matA = np.array([input().split() for _ in range(n)],int)

@author: DELL
"""

import numpy as np
n, m, p = map(int,input().split())
matA = np.array([input().split() for _ in range(n)],int)
matB = np.array([input().split() for _ in range(m)],int)

matA = np.reshape(matA,(n,p))
matB = np.reshape(matB,(m,p))
print(np.concatenate((matA, matB), axis = 0))


"""
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([5,6])
array_3 = numpy.array([7,8,9])
print(array_1)
print (numpy.concatenate((array_1, array_2, array_3))   )


array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print (numpy.concatenate((array_1, array_2), axis = 0)   )
"""