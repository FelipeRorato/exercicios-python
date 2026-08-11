nome = 0
preco = 1
estoque = 2
loja = [['camiseta roxa', 99.90, 100]]
def cadastrar_produto(catalogo: list[list[object]], nome: str, preco: float, estoque: int) -> list[list[object]]:
    """Cadastra um novo produto no catálogo.

        Args:
            catalogo: Catálogo atual de produtos.
            nome: Nome do produto.
            preco: Preço do produto.
            estoque: Quantidade disponível em estoque.

        Returns:
            O catálogo atualizado com os novos produto.
        """
    catalogo.append([nome, preco, estoque])
    return catalogo

def exibir_catalogo(catalogo: list[list[object]]) -> None:
    """Exibe todos os produtos do catálogo.

       Args:
           catalogo: Catálogo de produtos a ser exibido.

       Returns:
           None.
       """
    for produto in catalogo:
        print(
            f"{produto[nome]} - "
            f"R${produto[preco]} - "
            f"estoque: {produto[estoque]}"
        )
exibir_catalogo(loja)
