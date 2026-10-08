'''Crie uma TUPLA prenchida com os PRIMEIROS colocados da
tabela do Brasileirão na ordem de colocação. Depois mostre:
A) Apenas os 5 PRIMEIROS colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que POSIÇÃO na tabela esta o time da chapecoense.'''
times = ('Corinthians', 'Palmeiras', 'Santos',
         'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba',
         'Avai', 'Ponte Preta', 'Atlético Goianiense')
print('=' * 60)
print(f'\033[1;mTimes do Brasileirão:\033[m {times}')
print('\033[1;32m=\033[m' * 60)
print(f'Os 5 primeiros são: {times[0:5]}')
print('\033[1;32m=\033[m' * 60)
print('\033[1;31m=\033[m' * 60)
print(f'Os 4 ultimos colocados da tabela: {times[-4:]}')
print('\033[1;31m=\033[m' * 60)
print('=' * 60)
print(f'Em ordem alfabética {sorted(times)}')
print('=' * 60)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1} posição')


