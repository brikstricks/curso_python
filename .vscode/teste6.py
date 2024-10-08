"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nomeé {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} Letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba: "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrário é {nome[::-1]}')

    if ' ' in nome:
            print(f'Seu nome contém espaços')
    else:
            print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe você deixou campos vazios.")
