
from flask import Flask, jsonify, request, render_template

#Criando aplicaçao em flask!
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

#GET > Buscar algo
@app.route("/helloworld", methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estam voces"

    })

#Listas de tarefas
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False},
    {"id": 2, "titulo": "Ler a doc", "feito": True}
]
#GET > Buscar algo

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

#POST > Criar algo
    """
    javascript(front)->fetch
    ReactJS(front)->axios
    Insomnia(Aplicativo)->simula um front-end
    Postman(Aplicativo)->simula um front-end
    Back-end -> Modelo de API -> FULL REST
    Full-Stak -> Arquitetura MVC (Model, View, Controller)
    """
@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json
    nova_tarefa['id'] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(tarefas), 201

#Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

    #http://localhost:5000/helloworld
    #http://localhost:5000/tarefas


    