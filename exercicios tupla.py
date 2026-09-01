#ex1
notas = (7.5, 8.0, 6.5, 9.0)
print(notas[0])
print(notas[-1])

#ex2
numeros = (12, 45, 7, 23, 9, 31)
total = 0
for numero in numeros:
    total += numero
print(total)

#ex3
def contarpares(numeros1: tuple):
    total = 0
    for numero in numeros1:
        if numero % 2 == 0:
            total += numero
    return total
print(contarpares((12, 45, 7, 23, 9, 31)))

#ex4
produtos_loja1 = ("Caneta", "Caderno", "Mochila")
produtos_loja2 = ("Estojo", "Régua")
todos_produtos = produtos_loja1 + produtos_loja2
print(todos_produtos)

#ex5
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
print(tupla[0:4])
print(tupla[6:9])
print(tupla[::-1])

#ex6
def calcular_maior_menor(tupladenumeros: tuple):
    print(f'maior numero: {max(tupladenumeros)}, menor numero: {min(tupladenumeros)}')
calcular_maior_menor((14,15,16,17))



