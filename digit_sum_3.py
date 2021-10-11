#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:16:51 2021

@author: nairuhi
"""

num = int(input())

last_digit = num % 10
middle_digit = num // 10 % 10
first_digit = num // 100

print(first_digit + middle_digit + last_digit)

