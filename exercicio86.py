print("Programa para contar quantas vezes o numero X aparece")
print()

# Entrada de dados
print()

valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

x = int(input("Informe o numero X: "))

print()

# Processamento
contador = 0
for i in range(len(valores)):
    if valores[i] == x:
        contador += 1

# Saída de dados
print(f"O numero {x} aparece {contador} vez(es) no vetor")

print()