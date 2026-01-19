n = float(input('Digite o valor do Salário: R$'))
print('Seu salário é de R$ {}, mas com o aumento de 15% você passará a ganhar R$ {}'.format(n, n + (n * 0.15)))

#profesor guanabara

salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {}'. format(salário, novo))