"""9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²

Tabela Condições IMC

  

 Abaixo de 18,5   | Abaixo do peso          

 Entre 18,6 e 24,9 | Peso ideal (parabéns)  

 Entre 25,0 e 29,9 | Levemente acima do peso

 Entre 30,0 e 34,9 | Obesidade grau I 

 Entre 35,0 e 39,9 | Obesidade grau II (severa)

 Maior ou igual a 40 | Obesidade grau III (mórbida)"""




peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = (peso/(altura)**2)

print("Seu IMC é", imc)
if imc <= 18.5:
    print("Você está abaixo do peso")
elif 18.6<=imc<=24.9:
    print("Você está no peso ideal, continue assim")
elif 25<=imc<=29.9:
    print("Você está levemente acima do peso")
elif 30<=imc<=34.9:
    print("Você tem Obesidade de grau I")
elif 35<=imc<=39.9:
    print("Você tem Obesidade de grau II")
else: 
    print("Você tem Obesidade de grau III")
