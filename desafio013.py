salario = float(input('Digite o valor do salário:R$'))
novo = salario + (salario * 15 / 100)
print('O salario atual que era de R${:.2f}, com o aumento de 15% passa a ser de R${:.2f}'.format(salario,novo))