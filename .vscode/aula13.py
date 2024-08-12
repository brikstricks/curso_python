nome = 'Pablo Lacerda Cassani'
altura = 1.65
peso = 74
# imc = peso / (altura * altura) # Desta forma da pra fazer também
imc = peso / altura ** 2 # Podemos utilizar a Procedência dos Operadores

print(nome, 'tem', altura, ',')
print('pesa', peso, 'quilos e seu IMC é:')
print(int(imc), '.') # int para tranformar o valor em inteiro.
print(imc, '.') # sem o int para deixar o valor com casas decimais