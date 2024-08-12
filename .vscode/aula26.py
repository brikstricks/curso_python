"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.:0>-100,.1f
Conversio Flags - !r !s !a __repr___str___ask
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{1000.628974651489742332:0=+10,.4f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
