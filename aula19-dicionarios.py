'''pessoas = {'nome': 'Marcelo', 'sexo': 'M', 'idade': 18} # para referênciar os elementos ultilizar colchetes {}
pessoas['nome'] = 'Leandro' # É possivel substituir um nome dentro de uma lista
pessoas ['peso'] = 98.5 # Tambem é possivel adicionar itens sem usar o append.
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # para declarar uultilizar chaves ()
print(pessoas.keys())                                      # Esse formato exige o uso de aspas duplas " "
print(pessoas.values())
print(pessoas.items())                       #BLOCO 1
for k in pessoas.keys():                     #EXERCICIOS
    print(k)
for v in pessoas.values():
    print(v)
del pessoas['sexo'] # posso ultilar del para excluir um item
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# Criando um Dicionário dentro de uma lista

'''brasil = []  #lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  #dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  #dicionário
brasil.append(estado1)
brasil.append(estado2)                   
print(estado1)                          #bloco 2
print(estado2)                          #EXERCICIOS
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['sigla'])'''


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #diferente das listas/tuplas que é utilizado o fatiamento com :, no dicionário usa-se COPY
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
    #for v in e.values():
        #print(v, end=' ')
    print()
