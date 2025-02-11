# converter temperatura de celsius para fahrenheit

print("digite 1 para  Ceusius, 2 para Fahrenheit, 3 para Kelvin")
opcao = int(input())

if opcao == 1:
    print("Conversor de temperatura de Fahrenheit para Celsius")
    print("Digite a temperatura em Fahrenheit: ")
    fahrenheit = float(input())

    formula = (fahrenheit - 32) * 5/9

    print("A temperatura em Celsius é: ", formula)

elif opcao == 2:

    print("Conversor de temperatura de Celsius para Fahrenheit")
    print("Digite a temperatura em Celsius: ")
    celsius = float(input())

    formula = (celsius * 9/5) + 32

    print("A temperatura em Fahrenheit é: ", formula)

elif opcao == 3:
    
        print("Conversor de temperatura de Celsius para Kelvin")
        print("Digite a temperatura em Celsius: ")
        celsius = float(input())
    
        formula = celsius + 273.15
    
        print("A temperatura em Kelvin é: ", formula)

else:
    print("Opção inválida")