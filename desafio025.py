'''Crie um programa que leia nome da pessoa e diga
 se tem "SILVA" no nome'''
nome = str(input('Digite o seu nome completo:')).strip()
print('O seu nome tem Silva? {}'.format('silva' in nome.lower()))