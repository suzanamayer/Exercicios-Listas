print("Programa para substituir caracteres especiais por -")
print()

# Entrada de dados
print()

frase = input("Informe uma frase: ")

print()

# Processamento
letras = "aeioubcdfghjklmnpqrstvwxyz"

resultado = ""
for i in range(len(frase)):
    if frase[i].lower() in letras:
        resultado += frase[i]
    else:
        resultado += "-"

# Saída de dados
print(f"Frase modificada = {resultado}")

print()