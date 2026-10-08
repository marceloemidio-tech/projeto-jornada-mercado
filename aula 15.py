'''n = s = 0
while True:
    n= int(input('Digite um numero: '))
    if n == 999:
        break # a função BREAK manda o programa parar uma função quando o objetivo é alcançado
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

# as fstring usa a técnica de interpulação. dentro do print usando um f minúsculo antes das aspas para simplificar o código.
# ao invés do usar o .format podemos usar a fstring.

                # outros exemplos de uso

'''nome = 'Marcelo'
idade= 43
print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) #PYTHON2'''

nome = 'Guilherme'
idade = 46
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R$:{salario:.2f}')