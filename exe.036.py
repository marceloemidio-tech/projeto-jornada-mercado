'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.O programa vai perguntar VALOR DA CASA,
o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, sadendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('\33[4:36:40m-=\33[m'*7)
print('\33[0:36:40m  Bank BLACK  \33[m')
print('\33[1:36:40m-=\33[m'*7)
casa = float(input('Qual o valor da casa? R$:'))
salario = float(input('Qual o seu salário? R$:'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('As prestações ficaram em R${:.2f} para pagar em {} anos'.format(prestacao, anos))
if prestacao <= minimo:
    print('Emprestimo \33[4:32:40mAPROVADO!\33[m')
else:
    print('Emprestimo \33[1:31:40mNEGADO!\33[m')
