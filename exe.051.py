'''Desenvolva um programa que leie o PRIMEIRO TERMO e a
RAZÃO de uma PA. (Progressão matemática) No final. mostre os 10 primeiros
termos dessa progressão'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end='  ')
print('Fim')