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



