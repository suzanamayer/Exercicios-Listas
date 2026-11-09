print("Programa para incluir um separador entre os caracteres")
print()

# Entrada de dados
print()

frase = input("Informe uma frase: ")
separador = input("Informe o separador: ")

print()

# Processamento
resultado = ""
for i in range(len(frase)):
    resultado += frase[i]
    if i < len(frase) - 1:
        resultado += separador

# Saída de dados
print(f"Frase com separador = {resultado}")

print()