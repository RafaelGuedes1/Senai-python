# def = funçao
# def carro_matheus():
   # print("pegeout 206 turbo")

#carro_matheus()

# def escrever_carro(nome):
   # print(nome)

#escrever_carro("mareia swap turbo")    

# def somar_numeros(num1, num2):
   # return num1 + num2

#resultado = somar_numeros(4, 4)
#print("Oresultado é:", resultado)

def verificaIdade(idade):
    if idade >= 18:
        return "pode ver o filme"
    else:
        return "nao pode ver o filme"
    
print("digite a idade")
idade = int(input())

resultado = verificaIdade(idade)
print (resultado)