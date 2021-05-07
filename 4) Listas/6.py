#Faça um Programa que peça as quatro alunos de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
#o número de alunos com média maior ou igual a 7.0.

aluno = []
nota = []
for i in range(1,3):
    print("Aluno {}\n".format(i))
    for j in range(1,3):
        nota.append(float(input("Digite a {} nota do aluno {}: ".format(j,i))))
aluno.append(nota[i]) 

print(nota)
print(aluno)

#for i in range(1,3):
   # print(nota[i])
    #soma = sum(nota[i])
    #print("Aluno media :",soma/4)