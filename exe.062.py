'''Melhore o DESAFIO 061.
Perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 TERMOS.'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= 10:
        print('{} > '.format(termo), end=' ')
        termo += razão
        cont += 1
    mais = int(input('Quer mostrar mais um termo? '))
print('FIM!')
print('Total de termos: {}'.format(total))
