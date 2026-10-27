print("Programa para salvar e apresentar 11 valores")
print()

# Entrada de dados
print()

valores = [0] * 11

for i in range(len(valores)):
    valores[i] = float(input(f"Informe o {i + 1}o valor: "))

print()

# Saída de dados
print("Valores informados")
for i in range(len(valores)):
    print(valores[i])
    print("----------------")

print()