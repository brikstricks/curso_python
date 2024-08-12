# Precedência dos Operadores

# 1. (n + n) => primeia coisa que será executado será o que está entre ()
# 2. ** => a segunda mais forte será a exponenciação
# 3. * / // % => depois, multiplicação, divisão, divisão inteira e módulo
# 4. + - => a última coisa que será realizado é a soma e subtração

conta_1 = 1 + 1 ** 5 + 5 # era para ser 1+1=2 elevado(** exponêncial)
                         # 5+5=10 no caso era para dar 1024. 
                         # porém o resultado foi 7.
print(conta_1)

# Então para que a conta saia como desejamos temos que deixar o código desta maneira:

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3)