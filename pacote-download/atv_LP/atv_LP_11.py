# 11. Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
# Centígrados.
#                           (Fahrenheit – 32) x 5
# Fórmula: Centígrados = ----------------------------
#                                      9

F = float(input("A temperatura está em quantos Fahrenheit: "))
C = ((F - 32) * 5) /9

print(f"A temperatura convertida para Graus Centígrados é {C}")