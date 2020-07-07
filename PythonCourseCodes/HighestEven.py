# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:41:34 2020

@author: anany
"""


def high_even (li):
    '''
    

    Parameters
    ----------
    li : Accepts a list of numbers
        DESCRIPTION.
        Performs %2 on elements to check evens then Max to return greatest even no.

    Returns
    -------
    TYPE
        Returns the greatest even number in the list

    '''
    return max(max_even for max_even in li if max_even%2 == 0)


print(high_even([2,6,3,7,2,9,26,3,4,90,2]))