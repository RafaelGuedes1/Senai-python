
class pessoa:

    #metodo construtor
    #é chamado quando criamos um objeto
    def __init__(self, nome, idade, altura):
        #atribuir a intidade
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olaá meu nome é {self.nome}  tenho {self.idade} anos, tudo isso de altura {self.altura} ')    



p1 = pessoa ("Rafael", 34, "1.50")
p2 = pessoa("Guilherme", 7, "1.35")
p3 = pessoa("Alberto", 18, "1.95")

p1.apresentar()
p2.apresentar()
p3.apresentar()
