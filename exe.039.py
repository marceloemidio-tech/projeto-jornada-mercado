'''Faça um programa que leia o ano de nascimento de u jovem e
informe de acordo com a idade:
- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento.
MOstrar tambem o tempo que falta ou que passou prazo'''

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu no ano de {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print(' Você deve se apresentar à junta militar de sua cidade'.format(nasc, idade, atual ))
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos'.format(saldo))
    ano = atual  + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))