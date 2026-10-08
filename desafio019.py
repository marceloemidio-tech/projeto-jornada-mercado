import random
nome1 = str(input('primeiro nome:'))
nome2 = str(input('segundo nome:'))
nome3 = str(input('terceiro nome:'))
nome4 = str(input('terceiro nome:'))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno sorteado foi:{}'.format(escolhido))