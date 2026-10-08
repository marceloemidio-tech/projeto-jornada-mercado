'''Refaça o DESAFIO 051.Lendo o PRIMEIRO TERMO
e a RAZÃO de uma PR.
mostrando os 10 PRIMEIROS TERMOS da progressão
usando a estrutura WHILE'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')