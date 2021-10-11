#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:37:23 2021

@author: nairuhi
"""

a1 = int(input("First member of arithmetic progression: "))
a2 = int(input("Second member of arithmetic progression: "))
n = int(input("Term numner n : "))

d = a2 - a1

an = a1 + ((n-1)*d)

print("The n-th member is: ", an)

