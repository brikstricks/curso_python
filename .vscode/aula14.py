nome = 'Pablo Lacerda Cassani'
altura = 1.65980234787
conta_banco = 105468
peso = 74
# imc = peso / (altura * altura) # Desta forma da pra fazer também
imc = peso / altura ** 2 # Podemos utilizar a Procedência dos Operadores

print(nome, 'tem', altura, ',')
print('pesa', peso, 'quilos e seu IMC é:')
print(int(imc), '.') # int para tranformar o valor em inteiro.
print(imc, '.') # sem o int para deixar o valor com casas decimais

linha_1 = f'{nome} tem {altura:.5f}, ' # :.2f é para estipular 
                                       # casas decimais
print(linha_1)

linha_1 = f'{nome} tem R${conta_banco:,.2f}. ' # :,.2f é para fazer a converção 
                                        # do número para Reais.
print(linha_1)
