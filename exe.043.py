'''Com o peso e a altura de uma pessoa,
calcule o IMC e mostre o seu status:
- Abaixo de 18.5 Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade mórbida'''
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é: {:.1f} ATENÇÂO!\n Você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f} PARABÉNS! \n Você está no Peso ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é de {:.1f} Consulte um médico\n Você está em Sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('{} CUIDADO! Obesidade')
else:
    print('{} CUIDADO! Obesidade Mórbida'.format(imc))