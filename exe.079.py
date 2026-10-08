'''Crie um program onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. caso o numero já exita lá dentro, ele não será adcionado.
No final, serão exibidos todos os valores em ordem crescente.'''
listanum = []
while True:
    l = int(input('Digite um valor: '))
    if l not in listanum:
        listanum.append(l)
        print('valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não sera adicionado na lista.')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
listanum.sort()
print(f'Você digitou os valores {listanum}')