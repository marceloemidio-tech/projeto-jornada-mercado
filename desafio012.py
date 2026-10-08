preço = float(input('Digite um valor:R$'))
novo = preço - (preço * 5 / 100)
print('O preço orinal R${:.2f},com 5% de desconto fica R${:.2f}'.format(preço,novo))

