print("Programa para exibir 18 numeros em ordem inversa")
print()

# Entrada de dados
print()

valores = [0] * 18

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

# Saída de dados
print("Numeros em ordem inversa")
for i in range(len(valores) - 1, -1, -1):
    print(valores[i])

print()