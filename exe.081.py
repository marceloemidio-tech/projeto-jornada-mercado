'''Crie um programa que vai ler vários numeros e colocar em uma lista.
depois mostre: A) Quantos numeros foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Você digitou os valores {len(valores)}')
valores.sort(reverse=True)
print(f'Em decrescente fica {valores}')
if 5 in valores:
    print('O valor 5 foi digitado na lista')
else:
    print(f'O valor 5 não foi digitado na lista')
