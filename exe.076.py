'''Crie um programa que tenha uma TUPLA única com nomes de produtos
 e seus respectivos PREÇOS, na sequência.
 No final mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem = ('Violão', 415,
            'Guitarra', 680,
            'Contra Baixo', 510,
            'Guaita', 28.50,
            'Cavaquinho', 290,
            'Mesa 4 canais', 1250,
            'Cajon', 94.50,
            'Amplificador', 900,
            'Cubo', 719.90)
print('_'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('_'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')