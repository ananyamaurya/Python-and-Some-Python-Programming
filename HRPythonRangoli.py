# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:52:01 2020

@author: anany
"""

n= int(input())

def drawRangoli(size):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    x=0
    if(size==1): print(alphabets[i-1])
    else:
    for i in range(size-1) :
        for j in range(size-1-i):
            print("--",end='')
        print('-'.join(alphabets[size-1:size-2-i:-1]),end='')
        if(i!=0): print('-',end='')
        print('-'.join(alphabets[size-i:size]),end='')
        for j in range(size-1-i):
            print("--",end='')
    print('-'.join(alphabets[size-1::-1]),end='-')
    print('-'.join(alphabets[1:size]),end='')
    for i in range(size-1) :
        for j in range(i+1):
            print("--",end='')
        print('-'.join(alphabets[size-1:i:-1]),end='')
        if(i!=size-2):print('-',end='')
        print('-'.join(alphabets[i+2:size]),end='')
        for j in range(i+1):
            print("--",end='')
    x='--------------------------------------------------'
    print(len(x))

drawRangoli(n)        