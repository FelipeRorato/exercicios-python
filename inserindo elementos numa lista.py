from operator import truediv

titulo = 'cadastro'
print(f'{titulo:^70}')

numeros = []
#lista vazia e cadastro com while True/ break
while True:
    n = int(input('entre com um número ou 0 para sair: '))
    if n == 0:
        break
    numeros.append(n)
print(numeros)
for item in numeros:
    print(item, end=' , ')