'''Laços de repetição. Conceito um'''

#for c in range(0, 7, 2):
 #   print(c)
#print('Fim')

#i = int(input('Inicio:'))
#f = int(input('Fim:'))
#p = int(input('Passo:'))
#for c in range(1, f+1, p):
 #   print(c)
#print('FIM')
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A somatória de todos os valores foi {}'.format(s))