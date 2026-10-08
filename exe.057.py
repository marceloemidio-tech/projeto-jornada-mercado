'''Faça um programa que leia o SEXO de uma pessoa. mas só aceite
 os valores 'M" ou 'F". Caso esteja errado, peça a digitação novamente
 até ter um valor correto.'''

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} foi registrado com sucesso!'.format(sexo))

