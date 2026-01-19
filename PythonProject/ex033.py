n = float(input('Digite um número'))
m = float(input('Digite outro número'))
o = float(input('Digite outro número'))

if n <  m and n > o:
    print('O maios valor é {}'.format(n))
if m < n and m > o:
    print('O maior número é {}'.format(m))
else:
    print('O maior número é {}'.format(n))
if o < n and o > m:
    print('O menor número é {}'.format(o))
if m < n and m > o:
    print('O menor número é {}'.format(m))
else:
    print('O menor número é {}'.format(n))

#professor guanabara

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando maior
maior =  a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))


