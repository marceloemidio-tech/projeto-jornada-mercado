'''Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA
para o estouro de fogos de artificio. Indo de 10 ATÉ 0. com
uma pausa de 1 SEGUNDO entre eles.'''
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('\33[4:33:40mFeliz ano novo!\33[m')