 # Faça um programa que solicita ao usuário um único número inteiro com três dígitos e exibe o
# número invertido.
# Exemplo:
# Informe um número com 3 dígitos: 136
# Número invertido: 631

num = int(input("Insira seu numero inteiro de 3 digitos:"))

centena = num // 100
#  o // retorna apenas o inteiro da divisao (no caso de 123 seria 1, por exemplo), entao assim extraimos o 1o algarismo

dezena = (num % 100) // 10
# primeiro retorna apenas o resto (%) e depois faz o msm processo para extrair a dezena

unidade = num % 10
# pega o resto que sobraria se dividisse o numero por 10 (que seria a casa da unidade)

numinv = unidade * 100 + dezena * 10 + centena

print(f"seu numero que antes era {num}, agora eh {numinv}")