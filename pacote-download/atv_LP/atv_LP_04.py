#4. Ler três valores numéricos e escrever a média aritmética.

n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva outro número: "))
n3 = int(input("Escreva outro número: "))

media = (n1 + n2 +n3)/3
print(media)

#com for
soma = 0
for x in range(3):
    n = int(input("Escreva um número: "))
    soma = soma + n

media = soma/3
print(f"A media da soma dos números é {media}")