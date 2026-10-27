print("Programa para somar posicoes impares e multiplicar posicoes pares")
print()

# Entrada de dados
print()

valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

# Processamento
soma_impares = 0
produto_pares = 1

for i in range(len(valores)):
    if i % 2 != 0:
        soma_impares += valores[i]
    else:
        produto_pares *= valores[i]

# Saída de dados
print(f"Soma dos valores nas posicoes impares = {soma_impares}")
print(f"Multiplicacao dos valores nas posicoes pares = {produto_pares}")

print()