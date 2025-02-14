"3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, "

A = int(input("Digite um número:"))
B = int(input("Digite um número:"))
if A == B:
    C = (A+B)
    print("Os dois números são iguais, portanto sua soma resulta em", C)
else:
    C = (A*B)
    print("O dois números são diferentes, portanto seu produto é", C)