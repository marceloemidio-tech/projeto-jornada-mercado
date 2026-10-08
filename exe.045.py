'''Crie um progra que faça o computador jogar
jokenpô com você'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1,2 )
print('''Suas opões:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('\33[1:33:40mJO\33[m')
sleep(1)
print('\33[1:36:40mKEN\33[m')
sleep(1)
print('\33[1:32:40mPO!!!\33[m')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == jogador or jogador == computador:
    print('\33[1:36:40mEMPATE\33[m')
elif jogador > computador:
    print('\33[4:32:40mVOCÊ GANHOU!\33[m')
else:
    print ('\33[1:33:40mO COMPUTADOR VENCEU!\33[m')
