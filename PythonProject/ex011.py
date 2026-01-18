n = float(input('Digite a autura da parede: '))
m = float(input('Digite a largura da parede: '))
o = n * m
p = float(1000 * o) / n
print('Sua parede tem a dimensão de {:.2f} X {:.2f} e sua area é de {:.3f}m²'.format(n, m, m*n))
print('Para pintar essa parede você precisará de {}ml'. format(p))