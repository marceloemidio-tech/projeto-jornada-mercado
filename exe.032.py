'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

from datetime import date

ano = int(input('Qual o ano que deseja pesquisar?:'))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de \33[1:32:40m{}\33[m é um ano BISSEXTO'.format(ano))
else:
    print('O ano de \33[1:31:40m{}\33[m não é um ano BISSEXTO'.format(ano))
