#Faça um programa que leia 5 números e informe o maior número. 
maior = 0 
for i in range (1,5):
    num = int(input(" Digite um numero: "))
    if num > maior: 
        maior = num 

print(maior)