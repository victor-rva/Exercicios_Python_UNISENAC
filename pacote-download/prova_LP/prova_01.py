"""
INSTRUÇÕES:
-Crie um arquivo com o seu nome para desenvolver a tarefa. Exemplo:  ivonei_marques.py
-Coloque o seu nome no início do arquivo como comentário.
-Quando finalizar envie este arquivo pelo blackboard, sem compactá-lo.
-Códigos iguais = D

COMPETÊNCIAS A SEREM AVALIADAS:
-Conseguir desenvolver uma solução viável para a tarefa proposta.
-Saber interpretar o que foi pedido.
-Saber utilizar os comandos de forma adequada.

TAREFA:
Faça um algoritmo em que leia infinitos números inteiros. O algoritmo finaliza ao ser digitado o número 0(zero) ou a palavra fim.
Se o número digitado for negativo, armazene em uma lista chamada lst_negativos.
     Quando finalizar o algoritmo, mostre todos os número negativos de lst_negativos, ou a mensagem:
     "Não foi digitado nenhum número negativo".
Se o número digitado estiver no intervalo entre 20 e 60, imprima a mensagem: "Número entre 20 e 60".
Se o número digitado estiver no intervalo entre 40 e 80 e for par, imprima todos o inteiros PARES entre o número digitado e 80, ou a mensagem: "Não há números inteiros neste intervalo".
Se o número digitado estiver no intervalo entre 40 e 80 e for ímpar, imprima todos os números inteiros IMPARES entre 40 e o número digitado, ou a mensagem: "Não há números inteiros neste intervalo."
Para os números que não estiverem nos intervalos acima mostrar a mesnagem: "Número Ok.".

EXEMPLO 1:
Digite um número: 44
     Número entre 20 e 60.
     Números PARES no intervalo de 44 a 80:
          46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78

EXEMPLO 2:
Digite um número: 63
     Números IMPARES no intervalo de 40 a 63:
          41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61

EXEMPLO 3:
Digite um número: 8
     Número Ok.

EXEMPLO 4:
Digite um número: 0
Números negativos digitados:
     -5, -11, -55
"""

# Victor Vecchio
lst_negativos = []
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero < 0:
        lst_negativos.append(numero)
    if numero > 20 and numero < 60:
       print("Número entre 20 e 60")
    if numero > 40 and numero < 80:
        if numero % 2 == 0:
            print(f"Números pares no intervalo de {numero} a 80")
            for x in range(numero, 80):
                if x % 2 == 0:
                    print(x)
        elif numero % 2 == 1:
            print(f"Números impares no intervalo de 40 a {numero}")
            for y in range(40, numero):
                if y % 2 == 1:
                    print(y)
        else:
            print("Não há números inteiros neste intervalo")
    if numero < 20 or numero > 80:
        print("Número Ok.")
print(lst_negativos)
