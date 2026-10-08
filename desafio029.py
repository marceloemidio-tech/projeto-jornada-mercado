'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
A multa vai custar R$7,00 por cada Km acima do limite,'''

import math
speed = int(input('Qual a velocidade do carro?'))
if speed > 80:
    multa = (speed-80) * 7
    print('{} km/h VOCÊ FOI MULTADO!  por ultrapassar o limite de 80km/h'.format(speed))
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('{} km/h Você esta dentro do limite de 80km/h'.format(speed))