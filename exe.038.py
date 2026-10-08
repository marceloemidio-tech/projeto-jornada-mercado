'''Escreva um programa que leia 2 DOIS NÚMEROS inteiros
e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são IGUAIS'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n2 < n1:
    print('O primeiro valor {} é MAIOR'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é MAIOR'.format(n2))
else:
    print(' Os valores {} e {} são iguais'.format(n1, n2))