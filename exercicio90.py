print("Programa para contar quantas vezes o numero X aparece")
print()

# Entrada de dados
print()

x = int(input("Informe o numero X: "))

print()

valores = [0] * 32

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

# Processamento
contador = 0
for i in range(len(valores)):
    if valores[i] == x:
        contador += 1

# Saída de dados
print(f"O numero {x} apareceu {contador} vez(es) no vetor")

print()