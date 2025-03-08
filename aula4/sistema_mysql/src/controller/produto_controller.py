from ..model.produto_model import ProdutoModel

produto_model = ProdutoModel()

def cadastrar_produto(nome, preco):
    return produto_model.insert_product(nome, preco)

def listar_produtos():
    return produto_model.get_all_products()

def atualizar_produto(produto_id, nome, preco):
    return produto_model.update_product_by_id(produto_id, nome, preco)

def deletar_produto(produto_id):
    return produto_model.delete_product_by_id(produto_id)

def buscar_produto_unico(produto_id):
    return produto_model.get_product_by_id(produto_id)
