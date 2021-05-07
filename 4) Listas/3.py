#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [] # precisa definir antes que é um vetor 


for i in range(0, 4):

   notas.append(float(input("Informe a nota do aluno: "))) #E necessario usar o Append - nota[i] não funciona


print(f"A média desse aluno é {sum(notas)/len(notas)}.")