'''Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.'''

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Verificando quem é MENOR
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O MENOR é {}'.format(menor))
#Verificando quem é MAIOR
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O MAIOR é {}'.format(maior))
#else: n3 > n1 and n3 > n2 and n3 < n1:
    #print('O numero {} é o maior que e {}'.format(n3, n1,n2))