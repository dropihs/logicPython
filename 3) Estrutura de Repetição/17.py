#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um numero para fatorar: "))
i = 0
contador = 1 
while i < num: 
    fatorial = num * (num-contador)
    contador = contador - 1 
    i = i + 1 

print("Fatorial: ", fatorial)
