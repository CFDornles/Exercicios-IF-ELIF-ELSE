# Criar um programa para aprovar um emprestimo bancário para a compra de uma casa. O programa terá que perguntar o valor da casa, o salário do comprador
# e em quantos anos ele irá pagar.
# Calcule o valor mensal da prestação, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor_casa = float(input('Qual o valor do imovel? R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
anos = int(input('Informe em quantos anos será pago o imóvel: '))

prestacao = valor_casa / (anos * 12)  # cálculo da prestação mensal

if prestacao <= (salario * 0.3):  # verifica se a prestação não excede 30% do salário
    print('Emprestimo Aprovado! Parabéns!')
    print('O valor da prestação mensal será de R$ {:.2f}.'.format(prestacao))

else:
    print('Emprestimo negado! O valor da prestação excede os 30% do seu salário.')

# Nesse programa, primeiro são solicitadas as informações necessárias para realizar o cálculo da prestação mensal: o valor da casa,
# o salário do comprador e em quantos anos ele pretende pagar o empréstimo. Em seguida, é feito o cálculo da prestação mensal e é verificado
# se ela não excede 30% do salário. Se a prestação for menor ou igual a 30% do salário, o programa exibe a mensagem "Empréstimo aprovado!"
# juntamente com o valor da prestação mensal. Caso contrário, é exibida a mensagem "Empréstimo negado. O valor da prestação excede 30% do salário.".
