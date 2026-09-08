#Dicionarops sao colecoes do tipo formulario
#chave: valor
#exemplo:
#Nome: Felipe
#Idade: 20
#Nao sao posicionais - nao tem indice
#permitem tipos de dados diferentes
#permitem valores repetidos, porem chaves sao unicas
#permitem inclusao, alteracao e exclusao, portanto, SÃO MUTÁVEIS
#simbolo {}

aluno = {'nome': 'Felipe', 'idade': '20', 'sexo': 'masculino'}
print(aluno)
print(type(aluno))

vazio = {}
print(vazio)
vazio['categoria'] = 'brinquedo'
print(vazio)

vazio['nome'] = 'dinossauro'
vazio['fabricante'] = 'estrela'
print(vazio)

vazio['nome'] = 'genius'
print(vazio)
print(vazio.pop('nome')) #elimina segundo uma chave
del vazio['categoria'] #elimina segundo uma chave, del é uma exclusao generica
vazio.popitem() #elimina o ultimo
vazio.update({'categoria': 'com caixa'}) #altera tbm
print(vazio)


vazio.clear() #limpa o dicionario
print(vazio)


for caracteristica in aluno:
    print(caracteristica)

for chave in aluno.keys():
    print(chave)

for valor in aluno.values():
    print(chave)


alunocopia = aluno.copy()
alunocopia.update({'nota': '8'})
print('copia', alunocopia)
print('original',aluno)


# Exercício 02
# Preencha um dicionário com as informações de 5 produtos. Utilize o nome do produto como chave e o
# preço como valor. Solicite os dados ao usuário. Percorra o dicionário e exiba o nome dos produtos com
# preço superior a R$ 50,00.

#ex1
pessoas = {}
for _ in range(5):
    cpf = int(input("Digite um cpf: "))
    nome = input("Digite um nome: ")
    if len(str(cpf)) != 11:
        print("cpf invalido")
        break
    else:
        pessoas[cpf] = nome
print(pessoas)



ex2={'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}
userchave = input('Digite a chave: ')
uservalor = float(input('Digite o valor: '))
ex2.update({userchave: uservalor})
for chave, valor in ex2.items():
    if valor > 50:
        print(chave)


# Exercício 3
# Preencha um dicionário com os dados de 5 alunos. Utilize o RM do aluno como chave e uma lista de
# três notas como valor. Solicite os dados ao usuário. Percorra o dicionário e exiba a média de cada
# aluno.

# cpfronaldo = input("Digite os cpf do ronaldo: ")
# cpfrogerio = input("Digite os cpf do rogerio: ")
# cpfrodrigo = input("Digite os cpf do rodrigo: ")
# cpfromario = input("Digite os cpf do romario: ")
# cpfrodinei = input("Digite os cpf do rodinei: ")
#
# listacpf = {'cpf ronaldo': cpfronaldo, 'cpfrogerio': cpfrogerio, 'cpfrodrigo': cpfrodrigo, 'cpfromario': cpfromario, 'cpfrodinei': cpfrodinei}
# print(listacpf)
