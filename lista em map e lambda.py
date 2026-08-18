def defdesconto(preco:float, desconto:float) -> float:
    return preco * (1 - desconto)

print(defdesconto(100,0.1))

descontolambda = lambda preco,desconto: preco * (1 - desconto)
print(descontolambda(100,0.1))

precos = [100, 250, 399.99]
descontos = [0.1, 0.2, 0.05]
precos_descontos = list(map(defdesconto,precos,descontos))
print(precos)
print(precos_descontos)

