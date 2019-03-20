'''Escreva uma expressão em Python que atribua à variável c

a)O comprimento da hipotenusa em um triângulo
direito, cujos outros dois lados têm comprimentos 3 e
4
b)O valor da expressão booleana que avalia se o
comprimento da hipotenusa acima é de 5
c)A área de um disco de raio 10
d)O valor da expressão booleana que verifica se um
ponto com coordenadas (5, 5) está dentro de um
círculo com centro (0,0) e raio 7.'''
import math
 
b = 3
c = 4
h = math.sqrt(b*b+c*c)
print("Valor da hipotenusa:")
print(h)

tf = h>5
print("Valor da hipotenusa é maior que 5?")
print(tf)

pi = math.pi
r = 10
a = (pi*r*r)
print ("Area do disco:")
print(a)

raio = 7
kx = 5
ky = 5
eq = math.sqrt((kx*kx) + (ky*ky))
print("O ponto (5,5) pertence a área do circulo?")
print(eq<=7)