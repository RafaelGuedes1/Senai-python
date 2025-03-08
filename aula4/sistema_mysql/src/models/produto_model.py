class ProdutoModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_product(self, nome, preco):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
        self.db_connection.commit()
        return cursor.lastrowid

    def list_products(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, nome, preco FROM produtos")
        return cursor.fetchall()