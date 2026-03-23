# Escreva um programa que solicita ao usuário dois números inteiros e armazena nas variáveis A e B.
# Troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
# Ao final exiba na tela os valores que ficaram armazenados nas variáveis A e B respectivamente.

A = float(input("Insira o valor de A:"))
B = float(input("Insira o valor de B:"))
C = float(input("Insira o valor de C:"))

A, B, C = C, B, A

print("A =", A)
print("B =", B)
print("C =", C)