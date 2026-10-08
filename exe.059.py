'''Crie um programa que leie DOIS VALORES e
mostre um MENU na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar
a operação solicitada em cada caso'''
from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''\033[1;32m    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa\033[m''')
    print('\033[1;32m=-=\033[m' * 10)
    opção = int(input('\033[1;33;40m>>>>>Qual é a sua opção?\033[m'))
    if opção == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} vale {}'.format(valor1, valor2, soma))
    elif opção == 2:
        produto = valor1 * valor2
        print('O resultado de {} x {} é {}'.format(valor1, valor2, produto))
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} vale {}'.format(valor1, valor2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('\033[1;32m=-=\033[m' * 10)
sleep(2)
print('Fim do programa! Obrigado por utilizar!')

