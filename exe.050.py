'''DEsenvolva um programa que leia SEIS NÚMEROS INTEIROS
e mostre a soma apenas daqueles que forem PARES. Se o
valor digitado for ÍMPAR, desconsiderando o valor'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} PARES e a soma é {}'.format(cont, soma))

