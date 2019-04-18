# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:32:28 2019

@author: UNIP
"""
n = int (input ('Entre com o numero a qual deseja o fatorial: '))
fat = 1

for n in range (n, 0, -1):
    fat = fat * n
    print(fat)