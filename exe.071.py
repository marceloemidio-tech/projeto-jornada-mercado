'''Crie um programa que sinule o funcionamento de uma
 caixa eletronico. No inicio, pergunte ao usuário qual será o
 VALOR A SER SACADO (número inteiro) e o programa vai informar
 quantas CÉDULAS de cada valor serão entregues.
 obs: Considere que caixa possui cédulas de 50,20,10 e 1.'''
print('=' * 40)
print('{:^40}'.format('McBlack360 BANK'))
print('=' * 40)
saque = int(input('Qual volor deseja sacar?:'))
total = saque
cédula = 50
totalcédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédulas += 1
    else:
        if totalcédulas > 0:
            print(f'Total de {totalcédulas} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédulas = 0
        if total == 0:
            break