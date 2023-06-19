#6. Fazer um algoritmo para ler dois números e mostrar o maior deles.

n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva outro número: "))

if n1 > n2:
    print(n1,"é maior do que", n2)

else:
    if n2 > n1:
        print(n2,"é maior do que", n1)
# elif n2 > n1:
#      print(n2,"é maior do que", n1)
    else:
        print("Números iguais.")


# Usando o for
lst_n = []
for x in range(2):
    numeros = int(input("Escreva um número: "))
    lst_n.append(numeros)

maior_n = 0
for numeros in lst_n:
    if numeros > maior_n:
        maior_n = numeros

print(f"O maior número é {maior_n}")