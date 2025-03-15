import csv
#criar e escrever em um arquivo
with open("dados.txt", "w", encoding="utf-8") as arquivo:
   #"w" vem de Write, que significa escrita

   arquivo.write("Nome, Idade, Cidade\n")
   arquivo.write("Alberto, 28, Arraial/RJ\n")
   arquivo.write("Matheus, 28, Cotia/SP\n")
   arquivo.write("Ana, 25, São Paulo/SP\n")

   #ler o conteudo
   #r -> read -> leitura

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteudo do Arquivo txt:")
    print(arquivo.read())


    #criando arquivo csv
    #csv -> comma separated values
    dados =[
        ["Nome", "Idade", "Cidade"],
        ["Alberto", 28, "Arraial/RJ"],
        ["Matheus", 28, "Cotia/SP"],
        ["Ana", 25, "São Paulo/SP"]
    ]
#criar e escrever em um arquivo csv
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

    #ler o conteudo
    #r -> read -> leitura  
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteudo do Arquivo csv:")  
    for linha in leitor:
        print(linha)


   
   