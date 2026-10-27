print("Programa para listar pessoas com 18 anos ou mais")
print()

# Entrada de dados
print()

nomes = [""] * 7
idades = [0] * 7

for i in range(len(nomes)):
    nomes[i] = input(f"Informe o nome da {i + 1}a pessoa: ")
    idades[i] = int(input(f"Informe a idade da {i + 1}a pessoa: "))
    print()

# Processamento
# Saída de dados
print("Pessoas com 18 anos ou mais")
for i in range(len(nomes)):
    if idades[i] >= 18:
        print(nomes[i])

print()