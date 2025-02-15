# Conversor de Temperatura

""" Solicite ao usuario para fornecer uma temperatura em graus 
converta essa temperatura em Fahrenheit """

print ("Digite a temperatura em graus Celsius")

celsius = float (input())


formula = celsius * 1.8 + 32

print ("temperatura é", formula)

#Celsius para Kelvin

print ("Digite a temperatura em graus Celsius")
celsius = float (input())

formula = celsius + 273

print ("temperatura e", formula)

#Fahrenheit para Kelvin

print ("Digite a temperatura em Fahrenheit")
fahrenheit = float (input())

formula = (fahrenheit - 32) * 5/9 +273.15

print ("Temperatura é", formula)

print ("Digite a temperatura em Kelvin")
kelvin = float (input())

formula = (kelvin - 273.15) * 9/5 + 32

print ("Temperatura e", formula)

