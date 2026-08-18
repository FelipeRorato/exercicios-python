#Lambda
#Função anônima (pequena - de uma linha só - função inline)
#A criação da função estar próxima do uso dela
#Versáteis
#Tem que tomar cuidado pra NÃO TENTAR RESOLVER TUDO COM LAMBDA
#Se fizer isso, o programa fica ilegível

#numa função tradicional fariamos:
def dobro(n:int) -> int:
    return n * 2

#uso
print(dobro(4))

#transformar em lambda
#sintaxe lambda <argumentos> : <expressão de retorno>
ldobro = lambda n: n * 2
print(ldobro(5))

#uso mais comum:
print((lambda n: n *2 ) (50))

#lambda condicional
#Tem um if embutido
#Função que diz qual o maior de 2 números

def maior(x,y):
    if x>y:
        return x
    else:
        return y

print(maior(5,4))
#transformando em lambda

lmaior = lambda x,y: x if x>y else y

print(lmaior(5,4))

#uso mais comum:
print((lambda x,y: x if x>y else y)(7,9))

#pode usar o print dentro do lambda, mas com cuidado

lmenor = lambda x,y: print(x) if x<y else print(y)
xpto = lmenor (9,0)

#a melhor solução
lmenor2 = lambda x,y: f'o numero menor é {x}' if x<y else f'o numero menor é {y}'

##EXERCICIO CRIAR DETECTOR DE PAR OU IMPAR COM LAMBDA

parouimpar = lambda x: 'par' if x%2==0 else 'impar'
print(parouimpar(10))

#Map é ima funcionalidade que permite aplicar
#uma função em todos os elementos de uma coleção
def dobro (n:int) -> int:
    return n * 2
numeros = [5, 10, 15, 34]

#da maneira roots
dobrados = []
for n in dobrados:
    dobrados.append(dobro(n))
print(numeros)
print(dobrados)

#com Map
#sintaxe map (nome da função, iteravel/coleção)
dobrados2 = print(map(dobro, numeros))
print(dobrados2)
#2o uso direto no print
print(list(map(dobro, numeros)))

print(list(map((lambda n: n*3), [23, 4, 876, -4])))