"20 - Faça um Programa que leia três números e mostre o maior deles."


A = input("Digite um número:")
B = input("Digite outro número:")
C = input("Digite outro número:")

if A > B and A > C:
    maior = A
    print("O maior número é", maior)
elif B > A and B > C:
    maior = B
    print("O maior número é", maior)
elif A == B == C:
    print("Os números são iguais")
else:
    maior = C
    print("O maior número é", maior)