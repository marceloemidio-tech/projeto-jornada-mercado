'''Crie um programa que tenha uma TUPLA com várias palavras
(sem acentos). Depois disso, vocÊ deve mostrar, para
cada palavras, quais são suas vogais.'''
palavras = ('poder', 'Larousse', 'livro', 'estudar',
            'pensar', 'objetivo', 'foco', 'resiliencia',
            'futuro', 'programador', 'artificial', 'inteligencia')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')