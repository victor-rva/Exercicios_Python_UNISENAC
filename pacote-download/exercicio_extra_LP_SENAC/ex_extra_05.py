#Faça um Programa que peça as quatro notas para
#10 alunos, calcule e armazene em um vetor(lista)
#a média de cada aluno.
#Imprima o número de alunos com
#média maior ou igual a 7.0.

lista_media = []
for alunos in range(3):
    lista_nota = []
    for notas in range(4):
        nota = float(input(f"Nota {notas+1} do aluno {alunos+1}: "))
        lista_nota.append(nota)

    for x in range(1):
        soma = sum(lista_nota)
        media = soma / 4
        lista_media.append(media)
print(lista_media)

alunos_media = 0
lista_acima_media = []
for medias in lista_media:
    if medias >= 7:
        alunos_media += 1
        lista_acima_media.append(alunos_media)
print(f"{alunos_media} alunos passaram!")


# jeito alternativo de fazer, usando dicionario ao inves de lista na primeira parte do código
# dic_alunos = {}
#
# for alunos in range(10):
#     nome = str(input(f"Digite o nome do aluno {alunos+1}"))
#     lista_notas = []
#     for notas in range(4):
#         nota = float(input(f"Nota {notas+1} do aluno {nome}:"))
#         lista_notas.append(nota)
#     media = sum(lista_notas) / len(lista_notas)
#     dic_alunos[nome] = media
#acima_media = sum(1 for media in lista_media if media >= 7)