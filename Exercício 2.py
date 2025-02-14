"2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo."

A = int(input("Digite um número:"))
numero =(A%2)
if numero == 1:
    print("O número", A, "é ímpar")
else:
    print("O número", A, "é par")

if A <= 0:
    print("O número é negativo")
else:
    print("O número é positivo")