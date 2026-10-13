# requests.get(url) : envia uma requisição GET para o endereço informado e devolve um objeto de resposta
# resposta.status_code : código numérico que indica se a requisição deu certo. Os mais comuns:
# 200 (OK): deu tudo certo, os dados estão disponíveis.
# 404 (NOT FOUND): o endereço/recurso pedido não existe.
# 500 (INTERNAL SERVER ERROR): ocorreu um erro do lado do servidor.

# resposta.json() : converte o conteúdo JSON da resposta em um dicionário

import requests

# try:
#     cep = input('Digite o cep: ')
#     response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
#     if response.status_code == 200:
#         dicionario = response.json()
#         if 'erro' in dicionario:
#             print('CEP inexistente')
#         else:
#             print(f"Rua: {dicionario['logradouro']}")
#             print(f"Bairro: {dicionario['bairro']}")
#     else:
#         print(f'Erro de requisição: {response.status_code}')
# except requests.exceptions.ConnectionError as erro:
#     print('Erro. Erro de Conexão com API')
# except Exception as erro:
#     print(f'Erro: {erro}')
#


try:
    moedas = input('Digite o par do cambio (ex: USD-BRL): ')
    respostaapi = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas}')
    if respostaapi.status_code == 200:
        dicionario = respostaapi.json()
        if 'erro' in dicionario:
            print('Moedas inexistentes')
        else:
            print(f"bid: {dicionario['bid']}")
            print(f"ask: {dicionario['ask']}")
    else:
        print(f'Erro ao puxar dados da api: {respostaapi.status_code}')

except requests.exceptions.ConnectionError as erro:
    print('Erro. Erro de Conexão com API')
except Exception as erro:
    print(f'Erro: {erro}')
