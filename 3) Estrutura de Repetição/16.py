#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

num = int(input("digite o termo que deseja encontrar: "))
ultimo = 1
penultimo = 1 
i=0
termo = ultimo + penultimo

if (num == 1) or (num == 2): 
    print("1")
else: 
    while i <= num or termo <= 500:
        termo = ultimo + penultimo
        penultimo = ultimo 
        ultimo = termo 
        i += 1 
        print(termo)

#falta corrigir 
