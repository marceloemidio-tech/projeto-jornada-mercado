'''Teste = \033[;30;41m
Teste = \033[4;33;44m
Teste \033[1;35;43m
Teste \033[30;42ma
Teste \033[m]
Teste \033[7;30m]'''

nome = 'Marcelo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo' :'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

#nome = 'Marcelo'
#print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#'''print('\033[;30;41mOlá mundo!\033[m')
#print('\033[4;33;44m;Olá MUNDP!\033[m')
#print('\033[30;42mOLÁ MUNDO!\033[m')
#print('\033[mOLÁ MUNDO!\033[m')
#print('\033[7;30mOLÁ MUNDO!\033[m')'''