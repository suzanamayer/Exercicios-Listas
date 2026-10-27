print("Programa para calcular a media das notas dos alunos")
print()

# Entrada de dados
print()

nomes = [""] * 5
notas = [0.0] * 5

for i in range(len(nomes)):
    nomes[i] = input(f"Informe o nome do {i + 1}o aluno: ")
    notas[i] = float(input(f"Informe a nota do {i + 1}o aluno: "))
    print()

# Processamento
soma = 0
for i in range(len(notas)):
    soma += notas[i]

media = soma / len(notas)

# Saída de dados
print(f"Media das notas = {media:.2f}")

print()
print("Alunos com nota menor que 7")
for i in range(len(nomes)):
    if notas[i] < 7:
        print(nomes[i])

print()