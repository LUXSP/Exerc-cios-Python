"8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente."

A = int(input("Digite um valor:"))
B = int(input("Digite um valor diferente:"))
C = int(input("Digite outro valor diferente:"))
ordem = [A, B, C]

if A == B or A == C or B == C:
    print("Os valores são semelhantes, tente novamente")
else:
    ordem.sort(reverse=False)
    print("A ordem é", ordem)