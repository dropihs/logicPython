#Faça um Programa que peça as quatro alunos de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
#o número de alunos com média maior ou igual a 7.0.

mediaAluno = []
soma = 0
for j in range(1, 3):
    soma = 0 
    for i in range(1,5):
        soma += float(input("Digite a {} nota do aluno {} : ".format(i,j))) 
    media = soma/4 
    mediaAluno.append(media)
for i in range (0, len(mediaAluno)):
    if mediaAluno[i] >= 7:
        print("Aluno {}: {} Aprovado".format(i+1, mediaAluno[i]))
    else:
        print("Aluno {}: {} Reprovado".format(i+1, mediaAluno[i]))

#Demorei mas consegui fazer(eu acho)
