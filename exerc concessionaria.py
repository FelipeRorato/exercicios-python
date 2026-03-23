#  Uma concessionária de veículos paga aos seus vendedores um salário base de R$ 2.500,00. Além
#disso, uma comissão de R$ 200,00 por cada carro vendido e 2% do valor total das vendas.
#Escreva um programa que solicite o nome do vendedor, a quantidade de carros vendidos e o valor
# total de suas vendas. O programa deve calcular e exibir o salário final do vendedor.
# Exemplo:
# Nome do vendedor: Paulo
# Quantidade de carros vendidos: 5
# Valor total das vendas: 300000.0
# O vendedor Paulo receberá um salário de R$ 9500.0


salarbase = 2500

nomevendedor = input("Qual o nome do vendedor?")

valorcarro = float(input("Qual o valor do carro vendido?"))

quantcarro = int(input("Quantos carros foram vendidos?"))

valortotvendas = quantcarro * valorcarro

comissporcarro = 200 + (valorcarro / 50)

salariofinal = salarbase + (quantcarro * comissporcarro)


print(f"O nome do vendedor: {nomevendedor} \nQuantidade de carros vendidos: {quantcarro} \nValor total das vendas: {valortotvendas}\nO vendedor {nomevendedor} vai receber um salario de: {salariofinal} ")
