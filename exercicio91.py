print("Programa para verificar numeros pares e impares")
print()

# Entrada de dados
print()

valores = [0] * 21

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}o numero: "))

print()

# Processamento
impares = []
for i in range(len(valores)):
    if valores[i] % 2 != 0:
        impares.append(valores[i])

impares.sort()

# Saída de dados
if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares")
    print("Numeros impares em ordem crescente:")
    for i in range(len(impares)):
        print(impares[i])

print()