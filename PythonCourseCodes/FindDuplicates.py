# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:09:17 2020

@author: anany
"""


li = ['a','b','c','d','e','b','d']

l = [num for num in set(li) if li.count(num)>1]

        
print(l)