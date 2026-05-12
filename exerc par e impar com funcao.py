#faca uma funcao que recebe um numero inteiro e retorna true se for par e false se for impar
N = int(input('Digite seu numero: '))
def par(N):
    if N % 2 == 0:
        return True
    else:
        return False

print(par(N))