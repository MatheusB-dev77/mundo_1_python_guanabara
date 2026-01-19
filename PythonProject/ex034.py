n = float(input('Qual o salário do funcionário'))

if n <= 5000:
    print('Quem ganha R${} passa a ganhar R${:.2f} agora.'.format(n, (n*1.15)))
elif n <= 7000:
     print('Quem ganha R${} passa a ganhar R${:.2f}'.format(n,(n * 1.12)))
else :
    print('Quem ganha R${} passa a ganhar R${:.2f}'.format(n, (n * 1.10)))

#professor guanabara

salario = float(input('Qual é o salário do funcionário'))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar r${:.2f} agora}'.format(salario, novo))


