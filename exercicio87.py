print("Programa para multiplicar os vetores X e Y")
print()

# Entrada de dados
print()

x = [0] * 8
y = [0] * 8

for i in range(len(x)):
    x[i] = int(input(f"Informe o {i + 1}o valor de X: "))

print()

for i in range(len(y)):
    y[i] = int(input(f"Informe o {i + 1}o valor de Y: "))

print()

# Processamento
# Saída de dados
print("Resultado de X * Y")
for i in range(len(x)):
    print(f"{x[i]} * {y[i]} = {x[i] * y[i]}")

print()