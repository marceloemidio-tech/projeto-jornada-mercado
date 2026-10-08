'''Escreva um programa que pergunte o salario de um funcionário
e calcule o valor do seu aumenento
Para salarios superiores a R$1.250,00, calcule um aumento de 10%
Para inferiores ou iguais, o aumento é de 15%'''
import math
salario = float(input('Qual o valor do seu salário? R$:'))
n1 = salario + (salario * 15 / 100)
n2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print('O seu salario que era de R$:\33[1:31:40m{}\33[m passa a ser de R$:\33[1:32:40m{}\33[m'.format(salario, n1))
else:
    print('O seu salario que era de R$:\33[1:31:40m{}\33[m passa a ser de R$:\33[1:32:40m{}\33[m'.format(salario, n2))