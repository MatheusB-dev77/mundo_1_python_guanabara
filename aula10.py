"""nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print ('A sua média foi {:.1f}'.format(m))

if m >= 9.0:
    print('Excelente! Você é um ótimo Aluno(a)!!!')
elif m >= 8.0:
    print('Bom trabalho. Fique feliz com sua média')
elif m >= 7.0:
    print('Você passou de ano')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua Média foi {:.1f}'.format(m))
print('parabéns' if m >=6 else'estude mais!')



