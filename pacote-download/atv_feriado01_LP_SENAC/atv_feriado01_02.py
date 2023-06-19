"""
Faça um algoritmo que leia uma quantidade indeterminada de números positivos e maiores que zero.
A leitura dos números encerra ao digitar 0 (zero).
Quando for digitado um número negativo, mostre a seguinte mensagem: "Este número é negativo!"
Quando for digitado 0 (zero) mostre na tela o seguinte:
- Quantos números foram digitados que estão no intervalo entre 10 e 30.
- Mostre também todos os números que foram digitados no intervalo entre 20 e 50.
- Mostre quantos números negativos foram digitados.
"""
lst_n = []
lst_negativos = []
while True:
    try:
        numeros = int(input("Digite um número: "))
    except ValueError:
        print("Digite um valor válido")
        continue

    def remover_rep(lista):
        sem_rep = list(set(lista))
        return sem_rep

    if numeros > 0:
        lst_n.append(numeros)
    lst_n.sort()

    numero_sem_rep = remover_rep(lst_n)
    numero_sem_rep.sort()

    if numeros < 0:
        print("Este número é negativo!")
        lst_negativos.append(numeros)
        continue

    if numeros == 0:
        print(lst_n)
        print()
        print(numero_sem_rep)
        print()

        print("Dentre os números digitados os que estão entre 10 e 30 são esses: ")
        for i, x in enumerate(numero_sem_rep):
            if 10 <= x <= 30:
                print(x, end="")
                if i < len(numero_sem_rep) - 1:
                    print(", ", end="")
        print()
        print("Dentre os números digitados os que estão entre 20 e 50 são esses: ")
        for i, y in enumerate(numero_sem_rep):
            if 20 <= y <= 50:
                print(y, end="")
                if i < len(numero_sem_rep) - 1:
                    print(", ", end="")
        break

print()
print(f"Os números negativos digitados foram: {lst_negativos}")


