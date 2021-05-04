#Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
soma = 0
for i in range (num1,num2):
    soma += i  
    print(i)

print("Soma: ", soma)