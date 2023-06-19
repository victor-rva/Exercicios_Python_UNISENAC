# 10. Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
#                                       (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
# Cálculo da Média Ponderada = ------------------------------------------------------------------------
#                                                           soma dos pesos

n1 = float(input("Digite a nota1: "))
n2 = float(input("Digite a nota2: "))

peso_n1 = float(input("Digite o peso da nota1: "))
peso_n2 = float(input("Digite o peso da nota2: "))

soma = peso_n1  + peso_n2

calculo = ((n1 * peso_n1) + (n2 * peso_n2)) / soma

print(calculo)