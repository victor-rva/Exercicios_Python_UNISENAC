# Altere o exercício anterior (aula05) para ler o nome e o salário de 10 pessoas.
# Armazene em uma lista os nomes e os salários dos 3 maiores salários,
# armazene em outra lista os nomes e os salários dos 3 menores salários.
# Exercicío aula 05:
# Faça um algoritmo que leia o nome e o salário de 5 pessoas.
# Após digitar os dados, mostre o nome e o salário da pessoa que possui o maior salário.


# maior_sal = 0
# nome_maior_sal = ""
# lista_nomes = []
#
# for x in range (0,5,1):
#     nome = input("Nome da pessoa: ")
#     sal = float(input("Salário da pessoa: "))
#
#     if sal >= maior_sal:
#         if sal > maior_sal:
#             maior_sal = sal
#             nome_maior_sal = nome
#             lista_nomes.append(nome)
#
# print("Nome: ", nome_maior_sal)
# print("O maior salário é: ", maior_sal)


sal = 0
nome = ""
lista_nomes_sal = []
lst_n_s = []
lst_ordenada = []
for x in range(0, 10, 1):
    nome = input("Nome da pessoa: ")
    sal = float(input("Salário da pessoa: "))
    # lista_nomes.append(nome)
    # lista_sal.append(sal)
    lst_n_s = [nome, sal]
    lista_nomes_sal.append(lst_n_s)

print(lista_nomes_sal)

lst_ordenada = sorted(lista_nomes_sal, key=lambda y: y[1])

print(lst_ordenada)
for x in range(1):
    print(f"Os maiores salários são: {lst_ordenada[9]}, {lst_ordenada[8]}, {lst_ordenada[7]}")
    print(f"Os menores salários são: {lst_ordenada[0]}, {lst_ordenada[1]}, {lst_ordenada[2]}")

# for nome, sal in lst_ordenada:
#     print(f"Os maiores salários são: {lst_ordenada[9]}, {lst_ordenada[8]}, {lst_ordenada[7]}")
#     print(f"Os menores salários são: {lst_ordenada[0]}, {lst_ordenada[1]}, {lst_ordenada[2]}")







"""
FEITO EM AULA

Faça um algoritmo que leia o nome e o salário de
5 pessoas.
Após digitar os dados, mostre o nome e o salário
da pessoa que possui o maior salário.

# repetir 5 x
# Ler o nome de uma pessoa
# ler o salário de uma pessoa
n1 = input("Digite o nome da 1 pessoa: ")
s1 = float(input("Digite o salário da 1 pessoa: "))

n2 = input("Digite o nome da 2 pessoa: ")
s2 = float(input("Digite o salário da 2 pessoa: "))
n3 = input("Digite o nome da 3 pessoa: ")
s3 = float(input("Digite o salário da 3 pessoa: "))
n4 = input("Digite o nome da 4 pessoa: ")
s4 = float(input("Digite o salário da 4 pessoa: "))
n5 = input("Digite o nome da 5 pessoa: ")
s5 = float(input("Digite o salário da 5 pessoa: "))

# identificar o maior salário
if s1 > s2 and s1 > s3 and s1 > s4 and s1 > s5:
    print("Nome de quem ganha mais:", n1)
    print("Salário de quem ganha mais:", s1)
if s2 > s1 and s2 > s3 and s2 > s4 and s2 > s5:
    print("Nome de quem ganha mais:", n2)
    print("Salário de quem ganha mais:", s2)
if s3 > s1 and s3 > s2 and s3 > s4 and s3 > s5:
    print("Nome de quem ganha mais:", n3)
    print("Salário de quem ganha mais:", s3)
if s4 > s1 and s4 > s2 and s4 > s3 and s4 > s5:
    print("Nome de quem ganha mais:", n4)
    print("Salário de quem ganha mais:", s4)
if s5 > s1 and s5 > s2 and s5 > s3 and s5 > s4:
    print("Nome de quem ganha mais:", n5)
    print("Salário de quem ganha mais:", s5)
"""

"""
FEITO EM AULA - COM FOR

#Utilizando o for
maior_salario = 0
nome_maior_salario = ""
for x in range(5):
    n = input("Digite o nome da pessoa: ")
    s = float(input("Digite o salário da pessoa: "))

    if s >= maior_salario:
        maior_salario = s
        nome_maior_salario = n

print("Nome: ", nome_maior_salario)
print("Salário: ", maior_salario)


# maior_sal = 0
# nome_maior_sal = ""
# lista_nomes = []
#
# for x in range (0,5,1):
#     nome = input("Nome da pessoa: ")
#     sal = float(input("Salário da pessoa: "))
#
#     if sal >= maior_sal:
#         if sal > maior_sal:
#             maior_sal = sal
#             nome_maior_sal = nome
#             lista_nomes.append(nome)
#
# print("Nome: ", nome_maior_sal)
# print("O maior salário é: ", maior_sal)

lista_nomes_sal = []

for x in range(0, 10, 1):
    nome = input("Nome da pessoa: ")
    sal = float(input("Salário da pessoa "))
    lista_nomes_sal.append((nome, sal))

lista_nomes_sal.sort(key=lambda x: x[1], reverse=True)
# A função sort serve para ordenar a lista, a chave dela foi a palavra reservada "lambda" que recebe como
# entrada um tupla que contem o nome e o salário de uma pessoa, que foi representado pela variável x, depois a expressão
# retorna o segundo elemento da tupla. A função reverse serve para determinar se a lista será ascendente ou descendente.
maiores_sal = lista_nomes_sal[:3]
menores_sal = lista_nomes_sal[-3:]

print("Os 3 maiores salários são: ")
for nomes, sal in maiores_sal:
    print(f"{nomes}: - R${sal:.2f}")

print("Os 3 menores salários são: ")
for nomes, sal in menores_sal:
    print(f"{nomes}: - R${sal:.2f}")
#o ":.2f serve para indicar quantas casas depois dá virgula irão aparecer
"""