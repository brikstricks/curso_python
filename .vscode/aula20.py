"""
Exercício com valores em 'IF'
"""
primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} valor é maior ou igual '
        f'ao que {segundo_valor=}')
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}' 
    ) 