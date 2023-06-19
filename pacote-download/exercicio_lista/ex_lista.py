lista = []
menu = """

    Menu
    ------------------------------------------------
        1- Adicionar um número na lista
        2- Retirar um número da lista
        3- Alterar um elemento da lista
        4- Localizar um elemento e mostrar o seu indice
        5- Ler um indice e mostrar o elemento
        6- ler dois indices e mostrar a soma dos elementos;
    Escolha: """

while True:
    print(lista)
    escolha = input(menu)
    if escolha == "1":
        try:
            numero = int(input("Digite um número: "))
            lista.append(numero)
        except:
            print("OPS. Isto não é um número. ")
            continue
    if escolha == "2":
        try:
            numero_escolhido = int(input("Digite o número: "))
            lista.remove(numero_escolhido)
        except:
            input("OPS. Erro. Enter")
    if escolha == "3":
        while True:
            try:
                elemento = int(input("Digite o elemento que você deseja alterar na lista: "))
                if elemento in lista:
                    indice = lista.index(elemento)
                    lista[indice] = int(input("Digite o número: "))
                    break
                else:
                    print("Elemento não encontrado na lista!")
            except:
                print("Elemento inválido!")
    if escolha == "4":
        try:
            elemento = int(input("Digite o elemento que você deseja saber o indice: "))
            if elemento in lista:
                indice = lista.index(elemento)
                print(f"O elemento {elemento} está no indice {indice}")
            else:
                print("Elemento não encontrado na lista!")
        except:
            print("Elemento inválido!")
    if escolha == "5":
        try:
            indice = int(input("Digite o indice que você deseja saber o elemento: "))
            print(f"O índice {indice} possui o elemento {lista[indice]}")

        except:
            print("Elemento inválido!")
    if escolha == "6":
        try:
            indice1 = int(input("Digite o indice: "))
            indice2 = int(input("Digite o segundo indice: "))
            soma = lista[indice1] + lista[indice2]
            print(f"A soma entre os elementos dos índices {indice1} + {indice2} = {soma}")

        except:
            print("Elemento inválido!")
