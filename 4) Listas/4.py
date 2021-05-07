#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
a = [] 
for i in range(0,9):
    a.append(input("digite um caractere: "))
    if a[i] != 'a' and a[i] != 'e' and a[i] != 'i' and a[i] != 'o' and a[i] != 'u': 
        a[i] = a[i] + " é uma consoante"
        # print("Consoante")

print(a)