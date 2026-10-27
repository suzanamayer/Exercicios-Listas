print("Programa para encontrar valores comuns a dois vetores")
print()

# Entrada de dados
print()

vetor1 = [0] * 10
vetor2 = [0] * 12

for i in range(len(vetor1)):
    vetor1[i] = int(input(f"Informe o {i + 1}o valor do primeiro vetor: "))

print()

for i in range(len(vetor2)):
    vetor2[i] = int(input(f"Informe o {i + 1}o valor do segundo vetor: "))

print()

# Processamento
comuns = []
for i in range(len(vetor1)):
    if vetor1[i] in vetor2 and vetor1[i] not in comuns:
        comuns.append(vetor1[i])

comuns.sort(reverse=True)

# Saída de dados
print("Valores comuns em ordem decrescente")
for i in range(len(comuns)):
    print(comuns[i])

print()