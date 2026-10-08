'''Refaça o DESAFIO 009. mostrando a tabuada de um
número que o usuário escolher, só que agora
utilizando um Laço for'''

nun = int(input('Escolha um numero '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(nun, c, nun * c))