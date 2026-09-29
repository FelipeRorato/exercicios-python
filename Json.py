pessoa = {"nome" : "Felipe", 'idade' : '20', 'hobbies' : ['academia', 'jogos']}
print(type(pessoa))
print(pessoa)

#a biblioteca json vai pegar esse dicionario e transformar em um texto
#é bom pq na hora de gravar um arquivo, é preciso de texto

import json
#metodo dumps da biblioteca json converte uma coleção em um texto
pessoa2 = json.dumps(pessoa)
print(type(pessoa2))
print(pessoa2)


#o uso mais comum é gravar essas informações em um arquivo
#agora o método é dump (não dumps, em dumpS o S é de string)

with open('alunos.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos)

with open('alunos.json', 'a', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos, indent=4)

#acentuação
pessoanova = {"nome" : "Escobar", 'idade' : '40', 'hobbies' : ['empresariar', 'caçar animais']}
pessoanova = json.dumps(pessoanova, indent=4, ensure_ascii=False)
print(pessoanova)
# sem o parametro ensure_ascii o ç vai sair zoado

alunos={
    123456789:'{"nome" : "Escobar", "idade" : "40", "hobbies" : ["empresariar", "caçar animais"]}',
    987654321:'{"nome" : "Felipe", "idade" : "20", "hobbies" : ["academia", "jogos"]}'
}

with open('todosalunos.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(alunos, arqAlunos, indent=4, ensure_ascii=False)

#enquanto o dumps(string)/dump(arquivo) escreve no formato JSON,
#o loads(string)/load(arquivo) le do formato Json e coloca numa coleção

pessoatexto = '{"nome": "antonio nunes", "idade": "67", "hobbies": "praia"}'
print(type(pessoatexto))
print(pessoatexto)
#o metodo loads transforma essa string numa colecao
pessoadicionario = json.loads(pessoatexto)
print(type(pessoadicionario))
print(pessoadicionario)

#para ler um arquivo, precisa do método LOAD
