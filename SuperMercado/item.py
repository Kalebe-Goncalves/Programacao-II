class Item():
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

    def get_preco(self):
        return self.produto.preco * self.qtd