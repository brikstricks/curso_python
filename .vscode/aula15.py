a = 'AAAA'
b = 'BBBB'
c = 1.154435577
string = 'a={} b='
formato = string.format(a, b, c) # argumentos
print(formato)

string = 'a={} b={}'
formato = string.format(a, b, c) # argumentos
print(formato)

string = 'a={0} b={1} c={2:.5f}'
formato = string.format(a, b, c) # argumentos
print(formato)

string = 'a={0} a={0} a={0} b={1} c={2:.5f}'
formato = string.format(a, b, c) # argumentos
print(formato)

string = 'b={1} a={0} a={0} a={0} c={2:.7f}'
formato = string.format(a, b, c) # argumentos
print(formato)

string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.3f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    ) # argumentos

print(formato)
