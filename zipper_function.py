#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:28:40 2022

@author: julia
"""

food = ['pizza', 'sushi', 'jam']
people = ['Bob', 'Kevin', 'Angela']

def zipper(listA, listB):
    zipped = zip(listA, listB)
    
    return zipped

if __name__ == '__main__': # run directly the function
    
    food = ['pizza', 'sushi', 'jam', 'pho', 'tofu']
    people = ['Bob', 'Kevin', 'Angela', 'Meredith', 'Michael']
    
    result = zipper(food, people)
    for item in result:
        print(item)