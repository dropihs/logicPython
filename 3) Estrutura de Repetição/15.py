#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

num = int(input("digite o termo que deseja encontrar: "))
ultimo = 1
penultimo = 1 

if (num == 1) or (num == 2): 
    print("1")
else: 
    for i in range(2,num):
        termo = ultimo + penultimo
        penultimo = ultimo 
        ultimo = termo 
        i += 1 
        print(termo)