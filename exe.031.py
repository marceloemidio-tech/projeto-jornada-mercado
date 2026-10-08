'''Desenvola um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200Km
 e R$0,45 para viagens mais longas'''

distancia = float(input('Qual é a distância da viagem: '))
#if distancia <= 200:
 #  vl = 0.50 * distancia
#else:
 #  vl = 0.45 * distancia
#print('O valor da viagem ficou em R${:.2f}'.format(vl))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será R${:.2f}:'.format(preço))