'''Crie um programa que leia nome de uma cidade e diga
 se começa ou não com "SANTO"'''

cidade = str(input('Digite o nome de uma cidade:')).strip()
print(cidade[:5].upper() =='SANTO')