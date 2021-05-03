#8.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.








prod1 = float(input("Digite o preco do primeiro produto"))
prod2 = float(input("Digite o preco do segundo produto"))
prod3 = float(input("Digite o preco do terceiro produto"))



if prod1 < prod2 and prod1 < prod3:
    print("O produto mais barato eh o primeiro", prod1)
if prod2 < prod1 and prod2 < prod3:
    print("O produto mais barato eh o segundo", prod2)
if prod3 < prod1 and prod3 < prod2:
    print("O produto mais barato eh o terceiro", prod3)
