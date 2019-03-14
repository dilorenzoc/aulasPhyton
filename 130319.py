'''indice negativo'''
s = 'abcdefgh'
a = s[-3]
print(a)

'''printar intervalos'''
b = s[2:6]
print (b)

'''lista'''
lst = ['gato', 'cachorro', 3 ,64523651, 216585.955]
j = lst[-1]
print (j)

'''alteracao de lista'''
animais = ['formiga', 'morcego', 'bacalhau', 'cão', 'alce']
animais [2] = 'vaca'
print(animais)
'''metodos'''
animais.append('pintinho')
print(animais)
animais.reverse()
print(animais)
animais.pop()
print(animais)
p = animais.count('pintinho')
print(p)
animais.remove('alce')
print(animais)
animais.sort()
print(animais)
vaores