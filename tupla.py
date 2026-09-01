#tupla
#é uma coleção
#ela é IMUTAVEL: nasce e morre do mesmo jeito
#é posicional (indexada), ela é heterogenea

print('Tupla')
minhatupla= ('ceu', 'sol', 'mar')
print(minhatupla)

print(f'1a posicao: {minhatupla[0]}')
print(f'2a posicao: {minhatupla[1]}')
print(f'3a posicao: {minhatupla[2]}')
print(f'ultima posicao: {minhatupla[-1]}')

#nao faz sentido criar uma tupla vazia, pq nao vai dar pra colocar nada dentro depois
tuplavazia = ()
print(tuplavazia)

#sem a virgula, ele nao vira uma tupla (tupla de um elemento só)
tuplaumfalsa = ('ceu')
tuplaumreal = ('sol',)
print(tuplaumfalsa)
print(type(tuplaumfalsa))
print(tuplaumreal)
print(type(tuplaumreal))



#achando a posicao do elemento
minhatupla= ('ceu', 'sol', 'mar')
print(f'mar esta na posicao: {minhatupla.index('mar')}')
print(f'sol esta na posicao: {minhatupla.index('sol')}')
print(f'ceu esta na posicao: {minhatupla.index('ceu')}')

#achando posicao na tupla com repeticoes
minhatupla2 = ('ceu', 'sol', 'mar', 'mar', 'mar', 'sol', 'mar')
for indice, item in enumerate(minhatupla2):
    if item == 'mar':
        print(f'posicao {indice}: {minhatupla2[indice]}')


#matriz de tuplas
matrizdetupla = (('cafe', 'banho'), ('almoco', 'academia'), ('aula', 'series'))
print(matrizdetupla)
print(matrizdetupla[2][1])

