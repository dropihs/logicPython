#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
#elementos do vetor.

arrayA = []
for i in range(0,2):
    arrayA.append(float(input("Digite um numero")))

print(sum(arrayA)**2)