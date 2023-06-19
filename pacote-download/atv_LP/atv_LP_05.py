#5. Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.
"""
n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva outro número: "))
n3 = int(input("Escreva outro número: "))
n4 = int(input("Escreva outro número: "))
n5 = int(input("Escreva outro número: "))

s = n1 + n2 + n3 + n4 + n5
media = s /5
print(s,"," ,media)
"""

for x in range(0,5,1):
    print(x,"Lógica")

#for itera a variavel, por isso ela não precisa ser declarada antes
#range serve como o "enquanto", primeiro o python recebe o valor de zero, então o segundo númeor verifica se ele é maior do que o primeiro
#se for maior, ele consta como verdadeiro e executa a função; o terceiro número no () serve para adicionar ao zero, por isso ele irá se repetir 5 vezes

limite = int(input("Digite o limite do laço: "))
for x in range(limite):
    print(x,"Lógica")

limite = len("Lógica de programção")
for x in range(limite):
    print(x,"Lógica")

#len = conta o número de caracteres na string

texto = "Teste"
limite = texto
for x in range(limite):
    print(x,texto[x])

limite = int(input("Quantas vezes será repetido:"))
soma = 0
for x in range(limite):
    num = int(input("Digite um número:"))
    soma = soma + num
media = soma/ limite
print("A média é:", media)

soma = 0
for x in range(5):
    valor = int(input("Digite um valor: "))
    soma = soma + valor
media = soma / 5
print(f"A soma dos valores é {soma}")
print(f"A média dos valores é {media}")
