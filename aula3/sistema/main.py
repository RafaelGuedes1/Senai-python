from app.controllers.clienteController import ClienteController
from app.controllers.produtoController import ProdutoController

def exibir_menu():
    print("\n==== MENU ====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main():
    cntrCliente = ClienteController()
    cntrProduto = ProdutoController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            cntrCliente.criar_cliente(nome, email, idade)
        elif opc == "2":
            clientes = cntrCliente.listar_clientes()
            for index, cliente in enumerate(clientes, 1):
                print(f"{index}. {cliente}")
        elif opc == "3":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            cntrProduto.criar_produto(nome, preco, quantidade)
        elif opc == "4":
            produtos = cntrProduto.listar_produtos()
            for index, produto in enumerate(produtos, 1):
                print(f"{index}. {produto}")
        elif opc == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()