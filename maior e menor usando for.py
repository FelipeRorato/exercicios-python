
for i in range (5):
    n = int(input('Digite o número: '))
    if i == 0:
        maior = menor = n
        continue
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'o maior é: {maior}, e o menor é :{menor}')
