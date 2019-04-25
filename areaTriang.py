# -*- coding: utf-8 -*-
""" construir um programa para calcular a area de um triangulo qualquer. 
Equacoes: p=a+b+c/2 a=√p(p-a)(p-b)(p-c)

Use as listas contendo os lados dos triangulos para calcular as respectivas áreas
La=[5,10,15,20,25,30]
Lb=[3,6,9,12,15,18]
Lc=[4,8,12,16,20,24]
Created on Wed Apr 24 19:33:06 2019
@author:Camila Di Lorenzo
"""
import math

la=[5,10,15,20,25,30]
lb=[3,6,9,12,15,18]
lc=[4,8,12,16,20,24]

def formula (a,b,c):
    p = (a+b+c)/2
    area = math.sqrt(p*((p-a)*(p-b)*(p-c)))
    return area
    
comp = len(la)

for i in range (comp):
    medA = la[i]
    medB = lb[i]
    medC = lc[i]
    triangulo = formula(la[i], lb[i], lc[i])
    print(triangulo)