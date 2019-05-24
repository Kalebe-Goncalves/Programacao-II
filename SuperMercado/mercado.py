from produto import Produto
from item import Item
from carrinho import Carrinho

if __name__=='__main__':
    cafe = Produto('cafe', 5)
    cenoura = Produto('cenoura', 10)
    item_cafe = Item(cafe, 1)
    item_cenoura = Item(cenoura, 2.5)
    carrinho = Carrinho([item_cafe, item_cenoura])
    print('Preco correto cafe: {}'.format(item_cafe.get_preco()==5))
    print('Preco correto cenoura: {}'.format(item_cenoura.get_preco()==25))
    print('Preco correto carrinho: {}'.format(carrinho.get_preco()==30))
