#Faça um Programa que leia 20 números inteiros
#e armazene-os em uma lista.
#Leia a lista anterior e copie os números pares para a lista uma lista PAR
#e os números impares uma lista IMPAR.
#Imprima os três vetores(listas).

lista_numeros = []
lista_pares = []
lista_impares =[]

for x in range(20):
    try:
        numeros = int(input("Digite um número inteiro: "))
        lista_numeros.append(numeros)
    except ValueError:
        print("Escreva um número inteiro válido.")
    numeros2 = lista_numeros

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    if numero % 2 == 1:
        lista_impares.append(numero)

print(lista_numeros)
print(lista_pares)
print(lista_impares)
