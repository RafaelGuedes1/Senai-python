import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Substitua 'seu_usuario' pelo nome de usuário correto
    password="root",  # Substitua 'sua_senha' pela senha correta
    database="marea_toca_tudo"
)