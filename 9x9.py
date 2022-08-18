#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:41:48 2022

@author: lijiaheng
"""

#九九乘法

for i in range(1,10):
    for j in range (1,10):
        result = i * j
        print("%d x %d = %2d" %(j,i,result), end=("   "))
    print()

        