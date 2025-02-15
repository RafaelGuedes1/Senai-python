
#for x in range(10):
 #   print(x)

#faça a tabuada do 1 ao 10
for x in range(1,11):
    print("Tabuada do ", x)
    for y in range(1,11):
        print(x, "x", y, "=", x*y)  #concatenação de strings
    print("\n") #pula linha no final de cada tabuada
print("Fim da tabuada") #mensagem final 
