print("Programa para contar vogais, consonantes e outros caracteres")
print()

# Entrada de dados
print()

frase = input("Informe uma frase: ")

print()

# Processamento
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

qtd_vogais = 0
qtd_consoantes = 0
qtd_outros = 0

for i in range(len(frase)):
    letra = frase[i].lower()
    if letra in vogais:
        qtd_vogais += 1
    elif letra in consoantes:
        qtd_consoantes += 1
    else:
        qtd_outros += 1

# Saída de dados
print(f"Vogais = {qtd_vogais}")
print(f"Consoantes = {qtd_consoantes}")
print(f"Outros caracteres = {qtd_outros}")

print()