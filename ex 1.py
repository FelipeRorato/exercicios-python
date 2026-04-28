cont = 1
listapar = []
listaimpar = []
while cont <= 10:
    n = int(input('Digite um número para a lista: '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    cont += 1
print(listapar, listaimpar)