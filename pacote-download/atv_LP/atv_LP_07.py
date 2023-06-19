# 7. Ler 3 números e imprimi-los em ordem crescente.

lst_n = []
for x in range(3):
    n = int(input("Digite um número: "))
    lst_n.append(n)
lst_n.sort()
print(lst_n)