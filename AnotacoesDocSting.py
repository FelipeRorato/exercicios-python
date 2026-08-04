#Python tem tipagem dinamica

x = 10
print(type(x))
nome = 'paulo'
print(type(nome))

#type hints ajuda a definir o tipo de dados esperados na variavel
#mas é apenas uma AJUDA, ou seja, o python não impede que seja atribuido um
#valor com outro tipo de dado

nome: str = 'Paulo'
print(type(nome))

nome = 123
print(type(nome))

#todos os tipos de dados sao aceitos no type hints
#int, float, bool, str, list, etc

#o tipo mais importante é quando definimos funções
#quando definimos o tipo de dado esperado como parametro e tambem
#o tipo de retorno da função, estamos definindo a ASSINATURA DA FUNÇÃO
#isso é importante para disponibilizarmos essas funções, por exemplo,
#como API´s
def calcular_total(preco: float, quantidade: int) -> float:
    return preco * quantidade

print(calcular_total(10, 5))


def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")
#retorno eh None pq nao eh um tipo especifico que vai retornar (ex: "Leite - 8.9" nao é
#um tipo especifico)

exibir_produto('Leite', 8.9)


dadosPessoais = ['Felipe', 20, 'mto macho', 'superior']
print(dadosPessoais)
print(f"nome: {dadosPessoais[0]}")
print(f"idade: {dadosPessoais[1]}")

dadosPessoais.append('Aluno')
print(f"profissao: {dadosPessoais[4]}")