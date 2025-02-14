"7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO."

A = int(input("Digite um valor verdadeiro (1) ou falso (0):"))
B = int(input("Digite um valor verdadeiro (1) ou falso (0):"))
if A == 1:
    if B == 1:
        print("Ambos números são verdadeiros")
    elif B == 0:
        print("Apenas o primeiro valor é verdadeiro")
    else:
        print("Número inválido")
elif A == 0:
    if B == 0:
        print("Ambos os números são falsos")
    elif B == 1:
        print("Apenas o primeiro número é falso")
    else:
        print("Número inválido")
else:
    print("Número inválido")