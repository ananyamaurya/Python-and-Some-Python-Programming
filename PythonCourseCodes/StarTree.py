# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:55:18 2020

@author: anany
"""


l = [
     [0,0,0,1,0,0,0],
     [0,0,1,1,1,0,0],
     [0,1,1,1,1,1,0],
     [1,1,1,1,1,1,1],
     [0,0,0,1,0,0,0],
     [0,0,0,1,0,0,0]
     ]
for i in l:
    for j in i:
        if(j==0):
            print(' ',end='')
        if(j==1):
            print('*',end='')
    print('')