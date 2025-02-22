from ..models.cliente import Cliente
from ..database.database import bancofake

class ClienteController:
    def __init__(self):
        self.db = bancofake()

    def criar_cliente(self, nome, email, idade):
        id = len(self.db.listar_clientes()) + 1
        novo_cliente = Cliente(id, nome, email, idade)
        dict_cliente = {
            "id": novo_cliente.id,
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        self.db.adcionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        return self.db.listar_clientes()

