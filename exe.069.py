'''Leia a IDADE e o SEXO de vãrias pessoas. A cada pessoa cadastrada
o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres temmenos de 20 anos'''
total18 = totalH =totalM20= 0
while True:
    print('=' * 21)
    print('COMPLEMENTO CADASTRAL')
    print('=' * 21)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
            total18 += 1
    if sexo == 'M':
            totalH += 1
    if sexo == 'F' and idade < 20:
            totalM20 += 1
    tipo = ' '
    while tipo not in 'SN':
            tipo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if tipo == 'N':
        break
print(f'Total de {total18} pessoas com mais de 18 anos')
print(f'Temos ao todo {totalH} homens cadastrados')
print(f'Temos {totalM20} mulheres com menos de 20 anos')

