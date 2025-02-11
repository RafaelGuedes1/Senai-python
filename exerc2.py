# Caucule os numeros pares alternados de acordo com o numero que o usuario digitar

print("Digite um numero: ")
numero = int(input())

print("Digite o segundo numero: ")
numero2 = int(input())


for x in range(numero, numero2 + 1):
    if x % 2 == 0:
        print(x)
    else:
        continue