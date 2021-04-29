#7.	Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("digite um numero\n"))
num2 = int(input("digite outro numero\n"))
num3 = int(input("digite outro numero\n"))

maior = num1
menor = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

if menor > num2:
    menor = num2

if menor > num3:
    menor = num3

print('Maior: ', maior)
print('Menor: ', menor)
