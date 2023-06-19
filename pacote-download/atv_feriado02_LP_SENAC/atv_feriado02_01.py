"""
Exercício1.
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo
ao consumidor
"""

custo_fab = float(input("Valor do carro: "))
imposto = (custo_fab * 45) / 100
distribuidor = (custo_fab * 28) / 100
carro_novo = format(custo_fab + imposto + distribuidor, ".2f")

print(custo_fab)
print(imposto)
print(distribuidor)
print(f"O custo do consumidor será de: {carro_novo}")