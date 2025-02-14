"""16 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.""" 

numero1 = int(input("Informe um número inteiro:\n"))
numero2 = int(input("Informe outro número inteiro:\n"))
numero3 = int(input("Informe um número real:\n"))

print("O produto do dobro do primeiro com metade do segundo é:", (numero1*2)*(numero2/2))
print("A soma do triplo do primeiro com o terceiro é:", (numero1*3)+(numero3))
print("O terceiro número elevado ao cubo é:", (numero3**3))