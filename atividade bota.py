'''lst = [159.99,205.95, 128.83, 175.49]
a)Você encontrou outro
revendedor que vende as
botas por R$ 160,00; adicione
este preço à lista lst

b)Calcule o número de
varejistas que vendem as
botas por R$ 160,00

c)Encontre o preço mínimo em
lst

d)Usando c), encontre o índice
do preço mínimo na lista lst

e)Usando c) remover o preço
mínimo da lista lst

f)Classifique a lista lst em
ordem crescente'''

lst = [159.99,205.95, 128.83, 175.49]
lst.append(160.00)
fornecedor = lst.count(160.00)
print(fornecedor)
minimo = min(lst)
print(minimo)
indice = lst.index(minimo)
print(indice)
lst.remove(minimo)
lst.sort()
print(lst)
'''descobrindo o tipo da variavel'''
print(type(lst))
