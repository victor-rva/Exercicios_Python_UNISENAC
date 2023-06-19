# Faça um Programa que preencha uma lista com 10 números
# reais e mostre-os na ordem inversa.

lista_numeros = []
for x in range(10):
    numeros = float(input("Digite um número: "))
    lista_numeros.append(numeros)

print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)
