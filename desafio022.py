
nome = str(input('Digite o seu nome:')).strip()
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Tem {} letras'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é:{} e ele tem {} letras'.format(separa[0], len(separa[0])))
