'''Faça um programa que jogue PAR ou ÌMPAR com o computador.
O jogo só será interrompendo quando o jogadoe PERDER.
Mostrando o total de vitórias cosecutivas que ele
conquistou no final do jogo'''
from random import randint
from time import sleep
vitória = 0
while True:
    player = int(input('Escolha um numero entre 0 e 9: '))
    cpu = randint(1, 11)
    total = player + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar[P/I]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {cpu}. Toal de {total}', end = ' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            vitória += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            vitória += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Você venceu {vitória} vezes.')