'''Crie um programa que tenha uma TUPLA totalmente
preenchida com uma contagem por extenso de 0 até 20.
Seu programa deverá ler um numero pelo teclado e
mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'trez','quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    for range in cont:
        num = int(input('Digite um número ente 0 e 20:'))
       # print(f'Você digitou o numero {cont[num]}')
    if 0 <= num <= 20:
        break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o numero {cont[num]}')