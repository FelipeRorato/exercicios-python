def linear(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1

print(linear([12,10,20,30], 50))


def binaria(lista, n):
    inicio= 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == n:
            return meio
        elif n < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

print(binaria([10, 12, 15, 20, 30], 30))