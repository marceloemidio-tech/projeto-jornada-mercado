'''Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(totalmaior))
print('E tivemos {} pessoas MENORES de idade'.format(totalmenor))