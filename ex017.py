from math import hypot
n = float(input('Digite o cumprimeto do cateto opsto:'))
m = float(input('Digire o cumprimento do cateto adjacente:'))
print('A hipotenusa tem valor de {}'.format(hypot(n, m)))

#professor guanabara

co = float(input('digite o cateto opsto:'))
ca = float(input('digite o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.f}'.format(hi))

co = float(input('digite o cateto opsto:'))
ca = float(input('digite o cateto adjacente:'))
hi = hypot(co, ca)
