from math import hypot
co = float(input('comprimemnto do cateto oposto:'))
ca = float(input('comprimento do cateo adjacente:'))
hi = hypot(co, ca)
print(' O valor da hipotenusa é {:.2f}'.format(hi))