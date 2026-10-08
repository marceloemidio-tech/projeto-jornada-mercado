'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando número solicitado for negativo'''
while True:
    num = int(input('Qual o numero que você quer saber da taboada? '))
    if num == - num:
    #if num < 0: essa seria a forma mais limpa de fazer o código.
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('Fim da taboada')

