#Victor Vecchio


############ FUNÇÕES QUESTÃO 3 ############
def primeiro_da_lista():
    if algoritmo == listaA[0]:
        print("A disciplina que você escolheu é a primeira com mais letras")


def segundo_da_lista():
    if algoritmo == listaA[1]:
        print("A disciplina que você escolheu é a segunda com mais letras")


def terceiro_da_lista():
    if algoritmo == listaA[2]:
        print("A disciplina que você escolheu é a terceira com mais letras")


def quarto_da_lista():
    if algoritmo == listaA[3]:
        print("A disciplina que você escolheu é a quarta com mais letras")


def quinto_da_lista():
    if algoritmo == listaA[4]:
        print("A disciplina que você escolheu é a quinta com mais letras")


############ FUNÇÕES QUESTÃO 4 ############
def quantidade_numeros_final_zero():
    """
    Função feita para ver quantos números na listaB possuem o final com zero
    """
    terminam_com_zero = 0
    for x in listaB:
        if x % 10 == 0:
            terminam_com_zero += 1
    print(f"A listaB possui {terminam_com_zero} números que terminam com zero.")


############ FUNÇÕES QUESTÃO 5 ############
def conversao_inteiro_para_string():
    """lê um indice para a listaB. Se este indice for válido para a lista, converte o número que está
    nesta posição em uma string."""
    indice = int(input("Digite um número indicando o indice de elemento na listaB para tranforma-lo em string: "))
    if listaB[indice] in listaB:
        str(listaB[indice])
    print(listaB[indice])


############ FUNÇÕES QUESTÃO 6 ############
def tres_primeiras_letras():
    """
    Função para mostrar somente as três primeiras letras das disciplinas colocadas na listaA

    """
    for disciplina in range(1):
        if disciplina in listaA:
            print("As três primeiras letras de cada disicplina colocda na listaA são: ")
            print(disciplina[:3])










############ PROGRAMA PRINCIPAL ############

listaA = []
listaB = []

# Questão 1
#Faça um algoritmo para preencher a listaA com nomes
# das disciplinas do 1o semestre do seu curso.

while True:
    try:
        print("Para encerrar o programa digite 'FIM'.")
        disciplinas = input("Quais são as dicisplinas do seu primeiro semestre na faculdade? ").upper()
        if disciplinas == 'FIM':
            break
        listaA.append(disciplinas)
    except:
        print("ERRO, tente novamente!")

print(listaA)


# Questão 2
#Faça um algoritmo para preencher a listaB com números
# entre 100 e 500. A lista deve ficar com 10 números inteiros.
# - critério: Se for digitado algo diferente, mostrar a
# a seguinte mensagem: 'OPS. Só vale números entre
# 100 e 500'.

while True:
    numeros = int(input("Digite um número entre 100 e 500: "))
    if 100 <= numeros <= 500:
        listaB.append(numeros)
    if numeros <= 99 or numeros >= 501:
        print("OPS. Só vale números entre 100 e 500")
    if len(listaB) == 10:
        # listaB.remove(numeros)
        break
print(listaB)



# Questão 3
#Faça um algoritmo para escolher uma das disciplinas da listaA e
# imprima se a disciplina escolhida é a primeira, segunda,
# terceira, quarta ou quinta com mais letras.
#
# Exemplo: A disciplina que você escolheu é a segunda com mais letras.

while True:
    listaA.sort(key=len, reverse=True)
    # O argumento key=len especifica que a ordenação deve ser feita com base no comprimento de cada elemento.
    # O argumento reverse=True é usado para obter a ordem decrescente, da palavra com mais caracteres para a palavra com
    # menos caracteres.
    print("Para encerrar o programa digite 'FIM'.")
    algoritmo = input(f"Escolha uma das disciplinas da lista A para saber qual ordem ela está na lista com base na"
                      f"quantidade de caracteres que ela possuí (de primeiro a quinto lugar): {listaA}").upper()
    primeiro_da_lista()
    segundo_da_lista()
    terceiro_da_lista()
    quarto_da_lista()
    quinto_da_lista()
    if algoritmo == "FIM":
        break
    if algoritmo not in listaA:
        print("Disciplina não encontrada")


# Questão 4
#Faça um algoritmo que verifique na listaB quantos números
# terminam em zero(0)
quantidade_numeros_final_zero()


# Questão 5
#Faça um algoritmo que leia um indice para a listaB.
# Se este indice for válido para a lista, converta o número que está
# nesta posição em uma string.
conversao_inteiro_para_string()


# Questão 6
#Faça um algoritmo que mostre as 3 primeiras letras
# dos nomes das diciplinas da listaA.
tres_primeiras_letras()

