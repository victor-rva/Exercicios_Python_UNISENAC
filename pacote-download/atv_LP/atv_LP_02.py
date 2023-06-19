# 2. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
# variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
# conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.

vA = int(input("Escreva um número: "))

vB = int(input("Escreva outro número: "))
v1 = vA, vB
v2 = vB, vA

print(v1, v2)