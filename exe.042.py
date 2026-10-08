'''Refaça o exe.035 acrescentando o recurso de
 mostrar que tipo de triangulo ser formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
 '''
r1 = int(input('Digite o primeiro lado:'))
r2 = int(input('Digite o segundo lado:'))
r3 = int(input('Digite o terceiro lado:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos acima NÂO PODEM FORMAR um triangulo')