'''Leia o NOME e o PREÇO de vários produtos. Perguntado se o usuário vai continuar.
No final mostre:
A) Qual o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual o nome do produto mais barato.'''
total = mais1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço R$:'))
    cont += 1
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
      resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
      break
print(f'Total gasto na compra foi de R$: {total:.2f}')
print(f'{mais1000} custa mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa R$: {menor:.2f}')