matriz = []

for i in range(4):
    linha = []
    for j in range(3):
        nome = input(f"Digite o nome para posição [{i}][{j}]: ")
        linha.append(nome)
    matriz.append(linha)

print("\nMatriz final:")
for linha in matriz:
    print(linha)