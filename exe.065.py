'''Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado.
No final da execução mostre a A MÉDIA ENTRE TODOS os vslores e qual
foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao
usuário se ele quer ou não CONTINUAR a digitar valores'''
soma = quant = media = 0
#num = int(input('Digite um numero: '))
resp = 'S'
while resp in 'S':
    num = int(input('Digite numero: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Deseja digitar outro numero? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Foram digitados {} numeros e a média é {:.2f}'.format(quant, media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
