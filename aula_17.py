'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(5)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)  #Aqui os valores já estão definidos em lista
valores.append(9)
valores.append(4)
#print(valores)'''

'''valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posiçao {c} encontrei o valor {v}!')
print('Cheguei ao final !')'''

a = [2, 3, 4, 7]
b = a [:] # Cópia da lista. Cuidado para não ligar as listas
b[2] = 8
print(f'LIsta A:{a}')
print(f'Lista B:{b}')