import json
from pathlib import Path

class bancofake:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            with open(caminho, 'r', encoding="utf-8") as data:
                self.dados = json.load(data)
        else:
            self._salvar()
    
    def _salvar(self):
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            json.dump(self.dados, data, ensure_ascii=False, indent=4)

    def adcionar_cliente(self, client_direct):
        self.dados["clientes"].append(client_direct)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]

    def adicionar_produto(self, produto_dict):
        self.dados["produtos"].append(produto_dict)
        self._salvar()

    def listar_produtos(self):
        return self.dados["produtos"]
    
from ..models.produto import Produto
from ..database.database import bancofake

class ProdutoController:
    def __init__(self):
        self.db = bancofake()

    def criar_produto(self, nome, preco, quantidade):
        id = len(self.db.listar_produtos()) + 1
        novo_produto = Produto(id, nome, preco, quantidade)
        dict_produto = {
            "id": novo_produto.id,
            "nome": novo_produto.nome,
            "preco": novo_produto.preco,
            "quantidade": novo_produto.quantidade
        }
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        return self.db.listar_produtos()