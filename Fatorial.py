""" construir um programa em python para calcular o fartorial de um numero n solicitado na entrada de dados
Created on Wed Apr 17
@author: Camila Di Lorenzo Faria Saturnino"""

n = int (input ('Entre com o numero a qual deseja o fatorial: '))
if n < 0:
    print('Numero invalido!')
    
else:
    for i in range (n+1):
        if i == 0:
            fat = 1
        else: 
            fat = fat * i      
    print (fat)
    
    