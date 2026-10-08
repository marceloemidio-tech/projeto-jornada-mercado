nome = str(input('Digite seu nome: '))
if nome == 'Marcelo':
    print('Que nome bonito!{}'.format(nome))
elif nome == 'Mighel' or nome == 'Carlos' or nome == 'Paulo':
        print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Claudia Jéssica':
    print('Que belo nome feminino!')
else:
    print('O Seu nome é bem normal')
print('Tenha uma boa tarde!')