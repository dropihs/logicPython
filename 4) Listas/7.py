#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import numpy as np
num = []
for i in range(0,5):
    num.append(int(input("Digite um numero")))

print(num)
print("Soma: ",sum(num))
result = np.prod(num)
print("Multiplicação: ", result) #trapaceei usando numpy? depois faço do modo bruto 