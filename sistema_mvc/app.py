from flask import Flask
from flask_mysqldb import MySQL#biblioiteca para conexão com o banco de dados
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__)#inicia o Flask
app.config.from_object(config)#configura o Flask com as configurações do arquivo config.py


mysql = MySQL(app)#inicia o MySQL com as configurações do Flask

#passa a conexao para os controllers
app.mysql = mysql

#registra o controller
app.register_blueprint(produto_bp)

#Roda o app
if __name__ == '__main__':
    app.run(debug=True)
