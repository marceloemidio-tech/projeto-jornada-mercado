#tempo = int(input('Quantos anos tem o seu carro?'))
#if tempo <= 18:
 #   print('carro novo')
#else:
 #   print('carro velho')
  #  print('--FIM--')

                   #'''CONDIÇÃO SIMPLIFICADA'''

#print('carro novo'if tempo <= 3 else'carro velho')
#print ('--FIM--')
                #'''======================='''

#nome = str(input('Digite o seu nome:'))
#if nome == 'Marcelo':
 #   print('Que nome lindo você tem!')
#print('Bom dia, {}!'.format(nome))

                    #'''CONDIÇÃO COMPOSTA'''

#nome = str(input('Digite o seu nome:'))
#if nome == 'Marcelo':
 #   print('Que nome lindo você tem!')
#else:
  #  print('Seu nome é tão normal...')
#print('Tenha um bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nots:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('A sua média foi ruim... ESTUDE MAIS!')