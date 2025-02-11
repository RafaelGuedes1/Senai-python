print("Digite seu peso em KG: ")
peso= float(input())

print ("Digite sua altura em emtros: ")
metros = float(input())

imc= peso/(metros**2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")