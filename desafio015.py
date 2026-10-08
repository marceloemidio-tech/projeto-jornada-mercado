import math
km = int(input('Km:'))
dias = float(input('Dias:'))
#vkm = km * 0.15
#vd = dias = 60
valor = (dias * 60) + (km * 0.15)
#valor = (km * vkm) + (d * vd)
print('Valor R$:{:.2f}'.format(valor))
