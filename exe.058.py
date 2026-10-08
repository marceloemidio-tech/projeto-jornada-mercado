'''Melhore o jogo do DESAFIO 028 onde o computador vai pensar
em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar
adivinhar até acertar. mostrando no final quantos palpites
foram necessrios para vencer
'''
from random import randint
cpu = randint(0, 10)
print('\033[1;33m-=\033[m' *18)
print('\033[1;33;40mVou pensar em um numero entre 0 e 10\033[m')
print('\033[1;33m-=\033[m' *18)
acertou = False
palpites = 0
while not acertou:
    player = int(input('Escolha um numero entre 0 e 10: '.strip()))
    palpites += 1
    if player == cpu:
        acertou = True
    else:
        if player < cpu:
            print('MAIS... Tente mais uma vez')
        elif player > cpu:
            print('Menos... tente mais uma vez')
print('{} \033[1;32mVOCÊ ACERTOU!\033[m com \033[1;32m{} tentativas\033[m. E a CPU penseou o numero \033[1:32m{}\033[m'.format(acertou, palpites, cpu))