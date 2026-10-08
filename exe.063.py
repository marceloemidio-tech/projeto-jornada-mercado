'''Faça um programa que leia um número n inteiro
 e mostre na tela os n os primeiros elementos de uma
 SEQUÊNCIA DE FIBONACCI

 Ex: 1   1   2   3   5   8   13'''

print('\033[1;36;40m-\033[m' * 30)
print('\033[1;36;40mSequência de Fibonacci        \033[m')
print('\033[1;36;40m-\033[m' * 30)
num = int(input('Quantos termos?:'))
termo1 = 0
termo2 = 1
print('{} -> {}'.format(termo1, termo2), end='')
cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' -> FIM')
