import json #lidar com json
from pathlib import Path #lidar com caminhos do WIN



class bancofake:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        """Carrega dados do arquivo JSON, se existir. Caso nao exista, cria o arquivo
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            #abrindo arquivo no modo leitura em UTF-8 (pt-br)
            with open(caminho, 'r', encoding="utf-8") as data:
                #salvando dados que já existem no arquivo na variavel dados
                self.dados = json.load(data)
        else:
            self._salvar()
    
    def _salvar(self):
        """Salva os dados no arquivo JSON
        """
        #abrindo arquivo no modo escrita em UTF-8 (pt-br)
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            #realizando DUMP (Python para JSON)para salvar no banco
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


