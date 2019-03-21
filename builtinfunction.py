'''a)Solicite o nome do usuário
b)Solicite a Idade
c)Calcule a idade do usuário no próximo ano
d)imprima uma message se ele pode votar ou não'''
nome = input('Entre com seu nome: ')
sobrenome = input('Entre com seu sobrenome: ')
idade = int(input('Entre com sua idade: '))
voto = (idade>=16) 
line1 = 'Olá, ' + nome + ' ' + sobrenome + ', ano que vem você completará ' + str(idade+1) + ' anos!'
print(line1)
print('Pode votar? ' + str(voto))


