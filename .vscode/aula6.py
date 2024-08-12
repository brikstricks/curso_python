# Conservação de tipos, coerção
# type convertion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos:
#str, int, float, bool

# print(1 + 1)
# print('a' + 'b')
# print('a' + 1) # Vai apresentar erro pois podemos 
#                # juntar tipos diferentes.

# Outro exemplo

print(int('1'), type(int('1')))
print(float('1') + 1)
print(type(float('1.2') + 1))
print(bool('1.2'))
print(bool(''))
print(str(11) + 'b')