lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
for comidat in lanche:
    print(f'Eu vou comer {comidat}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi tudinho')