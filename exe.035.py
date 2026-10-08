'''Desenvolva um programa que leia o cumprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo'''

print('\33[1:33:40m-=\33[m'*13)
print ('\33[1:33:40m Analisador de Triangulo  \33[m ')
print('\33[4:33:40m-=\33[m'*13)
l1 = float(input('Primeiro valor: '))
l2 = float(input('Segundo valor: '))
l3 = float(input('Terceiro valor: '))
if l1 < l2 + l3 and l2 < l3 + l3 and l3 < l1 +l2:
    print('As linhas acima \33[1:32:40mPODEM\33[m formar um triângulo!')
else:
    print('As linhas acima \33[1:31:40mNÂO PODEM\33[m formar um triângulo')