#23.	Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
#  operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# .	par ou ímpar;
#a.	positivo ou negativo;
#b.	inteiro ou decimal.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

op = input("Qual operacao deseja realizar\n+(1)-(2)/(3)*(4)")

if op == '1':
    result = num1+num2
    print("A soma dos numeros é: ",result)
if op == '2':
    result = num1-num2
    print("A subtração dos numeros é: ",result)
if op == '3':
    if num1 == 0 or num2 == 0:
        print("0 não é divisivel")
    else:
        result = num1/num2
        print("A divisão dos numeros é: ",result)
if op == '4':
    result = num1*num2
    print("A produto da multiplicação é: ",result)

    
if result % 2 == 0:
    print("é par")
else: 
    print("é impar")    
    
if result > 0:
    print(result,"é um numero postivo")
elif result <= -1: 
    print(result,"é um numero negativo")



    
