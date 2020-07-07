# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:41:59 2020

@author: anany
"""


import numpy as np
li = []
n= int(input())
for i in range (n):
    li.append(list(map(float,input().split())))
print(np.linalg.det(li));