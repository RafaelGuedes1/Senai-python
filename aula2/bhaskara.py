#criar novo arquivo
# desenvolver um sistema que recebe
# valor de A, valor de B, e valor de C
# calcular a bhaskara
# Delta = b² - 4 * a * c
# calcule o valor de bhaskara
# x1 = (-b + raiz de delta) / 2 * a
# x2 = (-b - raiz de delta) / 2 * a

print("digite o  valor de a")
a = float(input())

print ("Digite o valor de b")
b = float(input())


print("Digite o valor de c")
c = float(input())

delta = (b**2) - 4 * a *c

raiz = delta ** 0.5

x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz ) / (2 * a)
print (delta)
print (x1)
print(x2)


# Desenvolver um sistema que recebe
# valor de A, valor de B, e valor de C
# calcular a Bhaskara
# Delta = b² - 4 * a * c
# Calcule o valor de Bhaskara
# x1 = (-b + raiz de delta) / (2 * a)
# x2 = (-b - raiz de delta) / (2 * a)

import math

print("Digite o valor de a")
a = float(input())

print("Digite o valor de b")
b = float(input())

print("Digite o valor de c")
c = float(input())

delta = (b**2) - 4 * a * c

if delta < 0:
    print("Delta é negativo, não existem raízes reais.")
else:
    raiz = math.sqrt(delta)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print("Delta:", delta)
    print("x1:", x1)
    print("x2:", x2)