# coleções sao variaveis de memoria que tem multiplos valores
#cada valor é chaado de item(elemento) que podem ser do mesmo tipo de dado
#ou de tipos diferentes: homogenea ou heterogenea

#Toda coleção é um elemento iteravel (pode ir de 1 em 1)

#há varios tipos de coleções: Listas, conjuntos(set), tuplas, dicionários(formulário, estrutura chave/valor)


#LISTA:
#a mais poderosa, pq é flexível, performática, e tem um conjunto de comandos para manipulação completos
#mutável: depois de criada, a lista permite acrescentar, retirar e modificar elementos
#Expansível: pode aumentar seu conjunto de dados a partir de outra lista
#aceita tipos diferentes de dados
#Indexada: cada elemento tem uma posição dentro da lista
#permite duplicados
#ordenáveis ---> ordenação natural só acontece se todos os eleentos forem do mesmo tipo
#símbolo: []


titulo = "listas"
print(f'{titulo:^70}')
minhalista = ['café', 'água', 'chá', 'açúcar', 'salsicha']
print(minhalista)

#e se eu quisesse imprimir só um?
#toda lista começa pelo 0

print(f'Quinto elemento: {minhalista[4]}')
print(f'tamanho da lista: {len(minhalista)}')

#como acrescentar itens na lista (métod o append)

print("\n")
print(minhalista)
minhalista.append('pumba')
print(minhalista)

#como remover itens da lista (métod o pop)

print("\n")
print(minhalista)
minhalista.pop()
print(minhalista)

#para remover um item espeífico com o pop, basta passar o índice

print("\n")
print(minhalista)
minhalista.pop(3)
print(minhalista)

#tod o elemento iterável podemos percorrer através do for

print("\n")
print("\n")
for item in minhalista:
    print(item)

print("\n")

for i in range(len(minhalista)):
    print(minhalista[i])


