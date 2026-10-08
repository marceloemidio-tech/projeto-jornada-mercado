'''Crie um programa que leie duas notas de um aluno e
calcule a sua média:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou suoerior: APROVADO'''
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('A sua média foi {:.1f} \n\33[1:31:40mREPROVADO!\33[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('A sua média foi de {:.1f} \nVOCÊ ESTÁ DE \33[1:33:40mRECUPERAÇÃO!\33[m'.format(media))
else:
    print('A sua média foi de {:.1f} \nPARABÉNS! Você foi \33[4:32:40mAPROVADO!\33[m'.format(media))