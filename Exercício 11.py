" 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7."

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))
media = ((nota1+nota2+nota3+nota4)/4)
print("A média das quatro notas é", media)

if media >= 7:
    print("Parabéns, você foi aprovado")
else: 
    print("Você foi reprovado")
