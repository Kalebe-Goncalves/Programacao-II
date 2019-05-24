class Carrinho():
    def __init__(self, itens):
        self.itens = itens
        
    def get_preco(self):
        preco = 0
        for item in self.itens:
            preco += item.get_preco()
        return preco
    