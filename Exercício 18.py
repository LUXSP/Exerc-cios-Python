"18 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."


peso = float(input("Qual é o peso dos peixes em Kg?\n"))
excesso = peso - 50
multa = float(excesso) * 4
if excesso >= 1:
    print("O valor a ser pago da multa, em reais, é:", multa)
else:
    print("Não será necessário pagar uma multa, pois o limite de peso não foi excedido")