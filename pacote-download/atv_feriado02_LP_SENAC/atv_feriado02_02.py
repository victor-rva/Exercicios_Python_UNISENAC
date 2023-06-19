"""
Exercício2.
Faça um algoritmo que leia um conjunto indeterminado de números inteiros
e mostre uma mensagem indicando se este número é par ou ímpar, e se é
positivo ou negativo. Terminar o programa quando o numero lido for 0 (Zero).
"""

while True:
    numeros = int(input("Digite um número inteiro: "))
    if numeros == 0:
        print("Programa encerrado")
        break
    if numeros % 2 == 0:
        print("Este número é par")
    elif numeros % 2 == 1:
        print("Este número é impar")
    if numeros > 0:
        print("Este número é positivo")
    elif numeros < 0:
        print("Este número é negativo")
