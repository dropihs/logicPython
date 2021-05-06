#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [ int(input("Informe a nota "+ str(i) ) ) for i in range(4) ]
print("Nota", notas)
print("Media", sum(notas)/4) 