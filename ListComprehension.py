# print('list comprehension')
#
# numeros = [4, 53, 87 ,43, 10]
# dobrados = []
# for numero in numeros:
#     dobrados.append(numero ** 2)
#
# print(dobrados)
# print('com o list comprehension')
# dobrados2 = [numero * 2 for numero in numeros]
# print(dobrados2)

#Exercicio 7
# use list comprehension para criar uma lista com os quadrados dos numeros de 1 a 10
quadrado = [n ** 2 for n in range (1,11)]
print(quadrado)

#Exercício 8
# Dada a lista numeros = [3, 8, 15, 22, 7, 40, 11],
# use list comprehension para criar uma nova lista contendo apenas os números pares.

numeros = [3, 8, 15, 22, 7, 40, 11]
pares = [n for n in numeros if n % 2 == 0]
print(pares)

# Exercício 9
# Dada a lista numeros = [3, 8, 15, 22, 7] , use list comprehension com expressão
# condicional ( if / else dentro da expressão) para criar uma lista com a string "par" ou
# "ímpar" correspondente a cada número, na mesma ordem
numeros = [3, 8, 15, 22, 7]
pareseimpares = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(pareseimpares)

#Exercício 10 (desafio)
# Você recebeu uma matriz de produtos, no mesmo formato usado no projeto de fundo
# ( [nome, preco, estoque] ): Use list comprehension para criar uma lista apenas com os nomes dos produtos que têm
# estoque menor que 10.
NOME, PRECO, ESTOQUE = 0, 1, 2
produtos = [
["Caderno", 12.50, 5],
["Caneta", 2.30, 100],
["Mochila", 89.90, 3],
["Estojo", 15.00, 8],
]
produtosestoquebaixo = [prod[0] for prod in produtos if prod[ESTOQUE]<10]
print(produtosestoquebaixo)