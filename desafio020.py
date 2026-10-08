import random

n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro nome:'))
n4 = str(input('Terceiro nome:'))
lista = [n1, n2, n3, n4]
escolhido = random.shuffle(lista)
print(escolhido)
print('A ordem de apresentação será:')
print(lista)