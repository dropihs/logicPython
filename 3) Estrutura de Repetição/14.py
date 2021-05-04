#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
qntimpar = 0
qntpar = 0
for i in range (1,11): 
    num = int(input("Digite um numero: "))
    if num %2 == 0: 
        qntpar = qntpar + 1
        print("O numero {} é par".format(num)) 
    else:
        qntimpar = qntimpar + 1 
        print("O numero {} é impar".format(num))     

print("A quantidade de numeros pares: ",qntpar)
print("A quantidade de numeros impares: ",qntimpar)
