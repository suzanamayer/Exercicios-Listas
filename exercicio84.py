print("Programa para apresentar numeros pares e impares")
print()

# Entrada de dados
print()

valores = [0] * 12

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

# Processamento
# Saída de dados
print("Numeros pares")
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i])

print()
print("Numeros impares")
for i in range(len(valores)):
    if valores[i] % 2 != 0:
        print(valores[i])

print()