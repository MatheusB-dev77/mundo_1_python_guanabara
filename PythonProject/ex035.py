n = float(input('Digite um segmento: '))
m = float(input('Digite outro segmento : '))
o = float(input('Digite um terceiro: '))

if n < m + o and m < n + o and o < n + m:
    print('Você tem um triângulo')
else:
    print('Você não tem um triângulo')

#professor guanabara
print('-= * 20')
print('Analisando um triângulo...')
print('-=-' * 20)


r1 = float(input('Digite um segmento: '))
r2 = float(input('Digite outro segmento : '))
r3 = float(input('Digite um terceiro: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você tem um triângulo')
else:
    print('Você não tem um triângulo')


