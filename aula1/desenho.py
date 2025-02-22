# Numeros pares em intervalo

# """ Solicite ao usuario para fornecer um intervalo de numeros
# e mostre todos os numeros pares dentro desse intervalo"""

print ("Digite o primeiro numero do intervalo")
num1 = int (input())

print ("Digite o segundo numero do intervalo")
num2 = int (input())

for x in range(num1, num2):
    if x % 2 == 0:
        print (x)
    else:
        continue

# Fim