# 12. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
# uma viagem até a casa de sua irmã.
# Dados extras:
# - Distância da casa de Maria até sua irmã : 520 km
# - Seu carro consome 12 Km/litro de combustível.
# - Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
# Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
# combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
# viagem e o custo da viagem.

distancia = float(input("Digite a distância: "))
consumo = float(input("Digite o consumo de km/litro de combustível do veículo por : "))
valor = float(input("Digite o valor do litro do combustível: "))

calculo1 = distancia / consumo
calculo2 = calculo1 * valor

print(f"A quantidade de litros de combustível usados na viagem foi de {calculo1}. O custo da viagem foi de {calculo2}")