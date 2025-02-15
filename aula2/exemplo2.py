# Sistema de descontos de veículos
# Solicite o nome do veículo
# e o preço do veículo
# Se o preço for > 80k -> 60% de desconto
# Se o preço for > 50k -> 30% de desconto
# Se o preço for < 30k -> não existe desconto

print("Bem-vindo ao cálculo de desconto")

print("Digite o nome do veículo")
nome_veiculo = input()

print("Digite o valor do veículo")
valor = float(input())

if valor > 80000:
    desconto = (valor * 60) / 100
    print(f"Seu desconto é de 60%: R$ {desconto:.2f}")
elif valor > 50000:
    desconto = (valor * 30) / 100
    print(f"Seu desconto é de 30%: R$ {desconto:.2f}")
else:
    print("Não existe desconto")

# Exibe o valor final após o desconto
if valor > 50000:
    valor_final = valor - desconto
    print(f"Valor final do veículo {nome_veiculo} após desconto: R$ {valor_final:.2f}")

