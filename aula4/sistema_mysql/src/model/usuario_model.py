import mysql.connector
from config import Config

class UsuarioModel:
    def __init__(self):
        self.config = Config()
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_users(self):
        query = "SELECT id, nome, email, idade FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_user(self, nome, email, idade):
        try:
            query = "INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (nome, email, idade))
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.IntegrityError as err:
            if err.errno == 1062:  # Código de erro para duplicidade de chave
                raise ValueError("O email já está em uso.")
            else:
                raise

    def get_user_by_id(self, user_id):
        query = "SELECT id, nome, email, idade FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def delete_user_by_id(self, user_id):
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def update_user_by_id(self, user_id, nome, email, idade):
        query = "UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s"
        self.cursor.execute(query, (nome, email, idade, user_id))
        self.connection.commit()
        return self.cursor.rowcount

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

