#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR 
# e os números IMPARES no vetor impar. Imprima os três vetores.

num = [] 
par = []
impar = []
for i in range(0,19):
    num.append(int(input("Digite um numero: ")))
    if num[i] %2 == 0: 
        par.append(num[i])
    else:
       impar.append(num[i]) 

print("Numeros digitados: ",num)
print("Numeros impares digitados: ",impar)
print("Numeros pares digitados: ",par)