'''Escreve um programa que faça o CPU "pensar" em um numero
inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador

O programa deverá escrever na tela se o usuario veunceu ou perdeu.'''

from random import randint
from time import sleep
cpu = randint(0, 5) #faz o computador 'pensar'
print('\033[1;33m-=-\033[m' * 16)
print('Vou pensar em um numero entre 0 e 5, Guess what..')
print('\033[1;33m-=-\033[m' * 16)
player = int(input('Digite um numero entre 0 e 5:'))#faz o jogador adivinhar
print('PROCESSANDO...')
sleep(2)
if player == cpu:
    print('\33[1;32;35[mYOU WON!\033[m')
else:
    print('\033[1:30:35mYOU LOST!\033[m Eu escolhi o numero {} e não o {}'.format(cpu, player))
