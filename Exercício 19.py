"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$"""


horas = float(input("Quantas horas você trabalha no mês?\n"))
valor = float(input("Quanto você recebe por hora?\n"))
total = horas*valor
print("+ Salário Bruto: R$", total)
print("- IR (11%): R$", (total*0.11))
print("- INSS (8%): R$", (total*0.08))
print("- Sindicato (5%): R$", (total*0.05))
print("= Salário Líquido: R$", (total - total*0.24))