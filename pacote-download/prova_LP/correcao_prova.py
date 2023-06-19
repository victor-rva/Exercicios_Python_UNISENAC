lst_negativos = []
while True:
    numero = input("\nDigite um número [0-Finaliza]: ")
    if numero == "fim":
        break
    numero = int(numero)
    if numero == 0:
        break

    if numero < 0:
        lst_negativos.append(numero)

    if numero > 20 and numero < 60:
        print("Número entre 20 e 60")

    if numero > 40 and numero < 80 and numero % 2 == 0:
        if numero == 78:
            print("Não há números inteiros neste intervalo")
        else:
            for n in range(numero+2, 80, 2):
                print(n, end=", ")

    if numero > 40 and numero < 80 and numero % 2 == 1:
        if numero <= 43:
            print("Não há números inteiros neste intervalo.")
        else:
            for n in range(41, numero):
                if n % 2 == 1:
                    print(n, end=", ")

    if numero < 20 or numero > 80:
        print("Número Ok.")

if len(lst_negativos) == 0:
    print("Não foi digitado nenhum número negativo")
else:
    print("Número Negativos digitados:")
    print(lst_negativos)