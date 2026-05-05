minhalista = []

minhalista.append('salsicha')
minhalista.append('34')
print(minhalista)
print(minhalista[1])

complemento = ['açúcar', 'água quente', 'canela']
print('\n')
print(complemento)

minhalista.extend(complemento)
print(minhalista)

print(f'a agua quente esta na posição: {minhalista.index('água quente')}')

minhalista.remove('34')
print(minhalista)

print(minhalista[2])

minhalista.insert(2, 'chantilly')
print(minhalista)


print('\nOrdenação nativa nativa do python')
print(minhalista)
print(sorted(minhalista))



print('\nOrdenação com método da classe list')
print(minhalista)
minhalista.sort()
print(minhalista)



print('\n com números')

meusnumeros = [1, 34, 76, -1, 44, 144, 240, 180, 280, 300, 305]
print(meusnumeros)
print('Ordenando temporariamente so para a impressado com o SORTED')
print(sorted(meusnumeros))
print('\n')
print('ordenando pra sempre com o .sort()')
print(meusnumeros)
meusnumeros.sort()
print(meusnumeros)
print(meusnumeros)