#verificar se a palavra é um palindromo
#caso  seja exiba "é palindromo"
#caso nao seja exiba "nao é um palindromo"
#a verificaçao deve ser case sensitive

print("Digite uma palavra")
texto = input()
if texto.lower() == texto.lower()[::-1]:# lower ou upper ignora se a letra é maiuscula, case sensitive
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")