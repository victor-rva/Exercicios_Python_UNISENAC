# Faça um Programa que preencha uma lista com 5 números inteiros.
# Após preencher a lista, mostre o índice e o elemento nesta posição .
lista_numeros = []
for x in range(5):
    try:
        numeros = int(input("Digite um número: "))
        lista_numeros.append(numeros)
    except ValueError:
        print("Digite um número inteiro válido")

print(f"Indice   Elemento")
for indice, elemento in enumerate(lista_numeros):
    print(f"{indice} - - - - - {elemento}")