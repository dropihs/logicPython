#22.	Faça um Programa que peça um número e informe se o número é
# inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('Digite um numero qualquer :'))

if(numero // 1 == numero): 
    print('\nNúmero inteiro !')
else:
    print('\nNúmero Decimal !')