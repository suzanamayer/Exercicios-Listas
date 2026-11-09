print("Programa para trocar caracteres de posicao")
print()

# Entrada de dados
print()

caracteres = [""] * 12

for i in range(len(caracteres)):
    caracteres[i] = input(f"Informe o {i + 1}o caractere: ")

print()

# Processamento
for i in range(0, len(caracteres), 2):
    auxiliar = caracteres[i]
    caracteres[i] = caracteres[i + 1]
    caracteres[i + 1] = auxiliar

# Saída de dados
print("Caracteres apos a troca")
for i in range(len(caracteres)):
    print(caracteres[i])

print()