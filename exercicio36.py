valor = int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do seu salário: '))
prazo = int(input('Digite em quantos anos quer pagar: '))
limite = salario*0.3
qtd_meses = prazo * 12
valor_parcela = valor / qtd_meses



if valor_parcela > limite:
    print(f'Infelizmente o financiamento foi negado, pois o valor da parcela ficou em {valor_parcela}, sendo que o limite seria de {limite} ')
else:
    print('Parabéns o financiamento foi aprovado')
