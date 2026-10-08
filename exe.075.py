'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
 em uma tupla. No final, mostre:
 A) Quantas vezes apareceu o valor 9.
 B) Em que posição foi digitado o primeiro valor 3.
 C) Quai foram os números PARES.'''
numero = (int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')))
print(f'Você digitou:{numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}° posição')
else:
    print(f'O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')