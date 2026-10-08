'''Faça um programa que leie o nome completo de uma pessoa,
mostrando em seguida oprimeiro e oultimo nome separadamente.
Ex: Ana Maria de Souza
primeiro=Ana
ultimo=Souza'''
n = str(input('Digite o seu nome:')).strip()
nome = n.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O seu último é: {}'.format(nome[len(nome)-1]))