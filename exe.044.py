'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vistta  DINHEIRO/CHEQUE: 10% de desconto
- À vista no CARTÃO: 5% de desconto
- Em até 2x NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros'''

print('{:=^40}'.format('LOJAS ARMAS´ZEN'))
preço = float(input('Preço das compras R$:'))
print('''FORMA DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] à vista artão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Como deseja pagar?:'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$:{:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R$:{:.2f} COM JUROS'.format(total, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$:{:.2f} vai custarR$:{:.2f}'.format(preço, total))

