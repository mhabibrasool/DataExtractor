# -*- coding: utf-8 -*-
"""
Created on % 22 NOV 2020
@author: Habib Rasool

File: binarytodecimal.py
"""

bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2**exponent
    exponet = exponent - 1
print("The integer value is", decimal)