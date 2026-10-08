'''Crie um programa que leia um numero inteiro
e mostre na tela se o valor é PAR ou ÍMPAR'''


num = int(input('Digite um numero:'))
if num % 2 == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é ÍMPAR'.format(num))