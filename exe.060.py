'''Faça um programa que leia um NÚMERO qualquer
 e mostre o seu FATORIAL.
ex:
 5! = 5x4x3x2x1=120'''
'''from math import factorial
num = int(input('Digite um numero:')) #FEITA COM MÓDULO
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''

n= int(input('Digite um numero:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))



