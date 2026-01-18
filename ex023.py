"""n = str(input('Digite um número'))
n.split()
unidade = n[3]
dezena = n[2]
centena = n[1]
milhar = n[0]
print('Analizando o número {}'.format(n))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))"""

#professor guanabara

num = int(input('Informe um número'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

