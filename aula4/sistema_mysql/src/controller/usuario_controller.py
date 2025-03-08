from ..model.usuario_model import UsuarioModel

usuario_model = UsuarioModel()

def cadastrar_usuario(nome, email, idade):
    try:
        return usuario_model.insert_user(nome, email, idade)
    except ValueError as e:
        print(e)
        return None

def listar_usuarios():
    return usuario_model.get_all_users()

def atualizar_usuario(usuario_id, nome, email, idade):
    return usuario_model.update_user_by_id(usuario_id, nome, email, idade)

def deletar_usuario(usuario_id):
    return usuario_model.delete_user_by_id(usuario_id)

def buscar_usuario_unico(usuario_id):
    return usuario_model.get_user_by_id(usuario_id)

