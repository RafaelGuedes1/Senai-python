from src.controller import produto_controller
from src.controller import usuario_controller

def exibir_menu_principal():
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU PRINCIPAL ====")
    print("1 - Menu de Produtos")
    print("2 - Menu de Usuários")
    print("0 - Sair")

def exibir_menu_produtos():
    print("\n==== MENU DE PRODUTOS ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar Produto Único")
    print("0 - Voltar ao Menu Principal")

def exibir_menu_usuarios():
    print("\n==== MENU DE USUÁRIOS ====")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuários")
    print("3 - Atualizar Usuário")
    print("4 - Deletar Usuário")
    print("5 - Buscar Usuário Único")
    print("0 - Voltar ao Menu Principal")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Não existem produtos cadastrados")

def cadastrar_produto():
    print("\n--- Cadastrar Produto --- ")
    nome = input("Digite o nome: ")
    preco = input("Digite o preço: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def opcao_atualizar_produto():
    print("\n--- Atualizando Produto ---")  
    produto_id = input("Digite o ID do Produto: ")
    nome = input("Digite o novo nome: ")
    preco = input("Digite o novo preço: ")
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0:
        print(f"Produto {produto_id} atualizado com sucesso!")
    else:
        print(f"Produto {produto_id} não encontrado!")

# Funções para o menu de usuários
def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    usuarios = usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")
    else:
        print("Não existem usuários cadastrados")

def cadastrar_usuario():
    print("\n--- Cadastrar Usuário --- ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    idade = int(input("Digite a idade: "))
    novo_id = usuario_controller.cadastrar_usuario(nome, email, idade)
    if novo_id:
        print(f"Usuário cadastrado com sucesso com o novo ID {novo_id}.")
    else:
        print("Erro: O email já está em uso.")

def opcao_atualizar_usuario():
    print("\n--- Atualizando Usuário ---")  
    usuario_id = input("Digite o ID do Usuário: ")
    nome = input("Digite o novo nome: ")
    email = input("Digite o novo email: ")
    idade = int(input("Digite a nova idade: "))
    linhas = usuario_controller.atualizar_usuario(usuario_id, nome, email, idade)
    if linhas > 0:
        print(f"Usuário {usuario_id} atualizado com sucesso!")
    else:
        print(f"Usuário {usuario_id} não encontrado!")

def menu_produtos():
    while True:
        exibir_menu_produtos()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar_produto()
        elif opc == "0":
            break
        else:
            print("Opção Inválida, Tente Novamente...")

def menu_usuarios():
    while True:
        exibir_menu_usuarios()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_usuario()
        elif opc == "2":
            listar_usuarios()
        elif opc == "3":
            opcao_atualizar_usuario()
        elif opc == "0":
            break
        else:
            print("Opção Inválida, Tente Novamente...")

def main():
    while True:
        exibir_menu_principal()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            menu_produtos()
        elif opc == "2":
            menu_usuarios()
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida, Tente Novamente...")

if __name__ == '__main__':
    main()
