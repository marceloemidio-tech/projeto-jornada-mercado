'''Crie um programa que leia vários numeros inteiros pelo teclado.
O programa só irá para quando o usuário digitar o valor 999. que é
a condição de parada. No final, mostre qauntos números foeram digitados
e qual foi a soma entre eles. (desconsiderando a flag).'''

n = soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e soma entre eles é {soma}')