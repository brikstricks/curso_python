"""
Operadores "in" e "not in"
Strings são interáveis
0 1 2 3 4 5
P a b l o
-6-5-4-3-2-1
"""
nome = 'Pablo'

# print(nome[-5])
# print(nome[2])

print('a' in nome)
print('w' in nome)
print('blo' in nome)
print(10 * '-')
print('a' not in nome)
print('w' not in nome)
print('blo' not in nome)

print(10 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')