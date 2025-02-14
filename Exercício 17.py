"""17 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""


altura = float(input("Qual é sua altura?\n"))
sexo = input("Qual seu sexo? Digite (em maiúsculo) M para masculino e F para feminino:\n\n")
if sexo == "M":
    print("Seu peso ideal é:", (72.7*altura) - 58)
elif sexo == "F":
    print("Seu peso ideal é:", (62.1*altura) - 44.7)
else:
    print("Valor incorreto. Digite apenas M ou F")