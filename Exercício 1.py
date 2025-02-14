"1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C."


A = int(input("Digite um número:"))
B = int(input("Digite um número:"))
C = int(input("Digite um número:"))

soma = (A+B)

print("A soma entre", A, "e", B, "é", soma)

if soma > C:
    print(soma, "é maior que", C)
else:  
    print(soma, "é menor que", C)


