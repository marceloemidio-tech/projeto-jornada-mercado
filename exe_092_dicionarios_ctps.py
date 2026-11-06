'''Crie um programa que leie nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade. com quantos anos a pessoa vai se aposentar (35 anos de contribuição)'''
from datetime import datetime
funcionario = dict()
funcionario['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.now().year - nasc
funcionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if funcionario['ctps'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salário'] = float(input('Salário R${:.2f}: '))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
print('=' * 50)
for k, v in funcionario.items():
    print(f' -{k} : {v}')


