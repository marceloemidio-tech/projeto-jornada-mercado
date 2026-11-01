'''Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
Seu app deverá analisar se a expressão passada está com os parenteses abertos e fechados
na ordem correta.'''
ex = str(input('Digite a expressão:'))
lista = []
for simbolo in ex:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua lista está válida!')
else:
    print('Error! Revise sua lista.')

