"""
Faça um algoritmo que leia (teclado) infinitos números inteiros.
Esses números irão preencher a lista "lista_geral" com, no máximo, 10 números (elementos).
Quando lista_geral estiver com os 10 números e o próximo for adicionado,
    deverás retirar o número que ocupa a posição 0 (zero) de lista_geral
    e, se este número for par deverá ser inserido em lista_pares e, se for ímpar,
    deverá ser inserido em lista_impares.
Quando lista_pares ou lista_impares estiverem completarem 5 elementos, a lista deverá ser iniciada
    novamente (retirado todos elementos).
Exemplo: se lista_impares completar 5 elementos, lista_impares = [], e inicia tudo novamente.
"""
lista_geral = []
lista_pares = []
lista_impares = []
while True:
    try:
        numeros = int(input("Digite um número: "))
        lista_geral.append(numeros)
    except ValueError:
        print("Digite um número inteiro válido")
        continue
    print(lista_geral)
    print(lista_pares)
    print(lista_impares)
    if len(lista_geral) > 9:
        novo_numero = lista_geral[0]
        lista_geral.remove(novo_numero)

        if novo_numero % 2 == 0:
            lista_pares.append(novo_numero)

        if novo_numero % 2 == 1:
            lista_impares.append(novo_numero)

    if len(lista_pares) > 5:
        lista_pares = []
        # print("Lista de pares esvaziada")

    if len(lista_impares) > 5:
        lista_impares = []
        # print("Lista de impares esvaziada"

    if numeros == 0:
        break

print(lista_geral)
print(lista_pares)
print(lista_impares)
