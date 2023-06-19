"""
Exercício3.
Faça um algoritmo que leia um número indeterminado de
valores inteiros e imprima:
- Quantos números pares maiores que 20 e menores ou
    igual a 50 foram digitados.
- Qual o percentual de números ímpares maiores que zero
    foram digitados.
- Quantos números negativos foram digitados e qual o
    menor número negativos digitado.
"""
lst_n1 = []
lst_n2 = []
lst_impares_maior_zero = []
lst_negativos = []
lst_vinte_cinquenta = []
while True:
    print("Para encerrar o programa digite 00")
    try:
        numeros = int(input("Digite um valor: "))
    except ValueError:
        print("Digite um valor válido")
        continue

    if numeros % 2 == 0:
        lst_n1.append(numeros)
        if 20 < numeros <= 50:
            lst_vinte_cinquenta.append(numeros)

    if numeros % 2 == 1:
        lst_n2.append(numeros)
        if numeros > 0:
            lst_impares_maior_zero.append(numeros)

    if numeros < 0:
        lst_negativos.append(numeros)
        lst_negativos.sort()

    if numeros == 00:
        print("Programa encerrado!")
        break

num_n1 = len(lst_n1)
num_vinte_cinquenta = len(lst_vinte_cinquenta)
num_n2 = len(lst_n2)
num_impar = len(lst_impares_maior_zero)
num_percentual = (num_impar/num_n2) * 100
num_neg = len(lst_negativos)

print(lst_n1)
print(lst_vinte_cinquenta)
print(lst_n2)
print(lst_impares_maior_zero)
print(lst_negativos)


print(num_n1)
print(num_vinte_cinquenta)
print(num_impar)
print(num_n2)
print(num_neg)
print()
print(f"Foram digitados {num_vinte_cinquenta} números pares que estão entre 20 e 50")
print(f"O percentual de números ímpares maiores do que 0 foi de {num_percentual}%")
print(f"Foram digitados {num_neg} números negativos. O menor negativo é {lst_negativos[0]}")
