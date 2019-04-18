""" 
Created on Wed Apr 17 19:51:03 2019

@author: Camila Di Lorenzo Faria Saturnino"""

l = [0,1,2,3,4]

def fatorial (n):
    for i in range (n+1):
        if i == 0:
            fat = 1
        else: 
            fat = fat * i
    return fat

for n in range (len(l)):
    fat = fatorial(l[n])
    print (fat)

for n in range (9, 0, 1):
    fat = fat * n
    print(fat)
