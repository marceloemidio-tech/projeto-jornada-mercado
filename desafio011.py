largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))
area = altura * largura
print('Sua parede tem a dimensão de {} x {} e uma area {}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa area você ira precisar de {:.2f}L de tinta'.format(tinta))