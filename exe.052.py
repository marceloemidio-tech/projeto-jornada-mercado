'''Faça um programa que diga se ele
 é ou não NÚMERO PRIMO'''
numero = int(input('Digite um numero:'))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;33m', end=' ')
        total += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('Por isso ele é numero PRIMO')
else:
    print('NÃO é um numero PRIMO')
#if numero % 2 == 0 and numero // numero == 1:
 #   print('O numero {} \33[1:31mNÂO\33[m é Primo'.format(numero))
  #  if numero == 2:
   #     print('O numero {} É um numero primo'.format(numero))
#else:
 #    print('O numero {} É um numero primo'.format(numero))
