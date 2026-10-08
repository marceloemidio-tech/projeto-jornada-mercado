'''Crie um programa que leia uma frase qualquer e diga
e ela é um palindromo. desconsiderandos os espaços
exemplo: APOS A SOPA '''
frase = str(input('Diga uma frase: ')).strip().upper()
print('A frase digitada foi {}'.format(frase))
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('SIM! é um PALINDROMO')
else:
    print('A frase digitada NÃO é um PALINDROMO!')

