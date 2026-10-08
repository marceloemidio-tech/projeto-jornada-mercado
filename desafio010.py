real = float(input('Quantos você têm? R$'))

dolar = real / 5.11
euro = real / 5.84
yuan = real / 0.75
bitcoin = real / 328.973
print('Com R${:.2f} reais você pode comprar \n${:.2f} dólares \n£{:.2f} euros \n${:0f} yuans \n{:.8f} biticoins'.format(real, dolar, euro, yuan, bitcoin))