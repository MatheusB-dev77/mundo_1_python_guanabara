import math
n = float(input('Digite o ângulo que vpcê deseja: '))
print('O ângulo de 30.0 tem o seno de {}'.format(math.sin(n)))
print('O ângulo de 30.0 tem o cosseno de {}'.format(math.cos(n)))
print('O ãngulo de 30.0 yem a tangente de {}'.format(math.tan(n)))

#professor guanabara

ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('o ãngulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cos = math.cos(math.radians(ângulo))
print('O ângulo de {} TEM COSSENO DE {:.2f}'.format(ângulo,cos))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem tangente de {:.2f}.'. format(math.ângulo, tangente))

from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ângulo))
print('o ãngulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cos = cos(radians(ângulo))
print('O ângulo de {} TEM COSSENO DE {:.2f}'.format(ângulo,cos))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem tangente de {:.2f}.'. format(ângulo, tangente))
