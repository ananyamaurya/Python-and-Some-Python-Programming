# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:04:27 2020

@author: anany
"""


import string
# Complete the solve function below.
def solve(s):
    #return string.capwords(s)
    return ''.join( (c.upper() if i == 0 or s[i-1] == ' ' else c) for i, c in enumerate(s) )
print(solve('hello world lol'))