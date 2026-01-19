nome = input('Digite seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))


n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro Valor'))
print('A soma vale{}'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1// n2
e = n1 ** n2
print('A soma é {},\n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d))
