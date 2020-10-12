# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
odd = ['1','3','5','7','9']

def minusNum(num):
    condition = True
    
    while condition and num >= 0:
        occurence = False
        if (num%2 == 0):
            for i in odd:
                
                if i in str(num):
                    occurence = True
            
                    break
            if occurence == False:
                condition = False
        num = num-1
        
    return num

def plusNum(num):
    condition = True
    
    while condition:
        occurence = False
        if (num%2 == 0):
            for i in odd:
                
                if i in str(num):
                    occurence = True
                    
                    break
            if occurence == False:
                condition = False
        num = num+1
        
    return num
                
    
    
def checkNum(num):
    x = plusNum(num)- num
    y = num - minusNum(num)
    if(x > y):
       return y-1
    else:
        return x-1
       

a = int(input())
li = []
for i in range(a):
    li.append(int(input()))
for i in range(a):
    print(f"Case #{i+1}: {checkNum(li[i])}")
    
