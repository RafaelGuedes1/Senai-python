# Calculadora de IMC
""" Solicite o peso em Kg e a altura do usuario em metros
calcule o IMC e informe a classificação do IMC"""

print ("Digite seu peso em Kg")
peso = int (input())

print ("Digite sua altura em metros")
altura = float (input())

imc = peso / (altura ** 2)

if imc < 18.5:
    print ("Abaixo do peso")

elif imc >= 18.5 and imc < 24.9:
    print ("Peso normal")

elif imc >= 25 and imc < 29.9:
    print ("Sobrepeso")

# Fim

print ("Digite seu peso em KG")
peso = int (input())

print ("Digite sua altura em metros")
altura = float (input())

imc = peso / (altura * 2)

print ("Seu IMC é: ", imc)
