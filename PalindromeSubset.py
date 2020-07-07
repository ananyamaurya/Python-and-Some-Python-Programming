#!/bin/python3

import math
import os
import random
import re
import sys

def isPalindrome(s): 
    return s == s[::-1]
def distinctSubstring(str): 
  
    # Put all distinct substring in a HashSet 
    result = []; 
  
    # List All Substrings 
    for i in range(len(str)): 
        for j in range(i + 1, len(str) + 1): 
  
            # Add each substring in Set 
            result.append(str[i:j]); 
  
        # Return the HashSet 
    return result;

nq = input().split()
n = int(nq[0])

q = int(nq[1])

s = str(input())

for z in range(q):
    abc=input().split()
    a=int(abc[0])
    b=int(abc[1])
    c=int(abc[2])
    t=0
    
    if(a==1):
        t=int(abc[3])
        l = []
        print(a,b,c,t)
        for i in range(b,c):
            if((ord(s[i])+t)>122):
                l.append(chr(97+ (ord(s[i])+t)%123))
            else:
                l.append(chr(ord(s[i])+t))
        if(b==0):
            print(str(''.join(l))+s[c:])
        else:
            s= str(s[:b]+str(''.join(l))+s[c:])
            print(s)
    if(a==2):
        if(b==0):
            count=0
            x= s[:c+1]
            w= distinctSubstring(x)
            for i in w:
                print(i)
                if(isPalindrome(i)):
                    count+=1
            print(count)
        else:
            x= s[b:c+1]
           # w= distinctSubstring(x)
           # for i in w:
           #     if(isPalindrome(i)):
            #        count+=1
            count = CountPS(x,len(x))
            print(count)
