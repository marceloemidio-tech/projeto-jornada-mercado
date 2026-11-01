'''Faça um progama que ajude um jogador da MEGA SENA a criar
 palpites. O programa vai perguntar quantos jogos serão
 gerados e vai sortear 6 numeros entre 1 e 60 para ca jogo,
 cadastrndo tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print('=~' * 15)
print('      BOLÃO DA MEGA SENA     ')
print('=~' * 15)
quantidade = int(input('Quantos jogos você quer fazer?: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {quantidade} JOGOS ')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
