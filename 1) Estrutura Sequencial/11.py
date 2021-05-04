#11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a.	o produto do dobro do primeiro com metade do segundo .
#b.	a soma do triplo do primeiro com o terceiro.
#c.	o terceiro elevado ao cubo.

num1 = int(input("Digite um numero inteiro"))
num2 = int(input("Digite outro numeoro inteiro"))
num3 = float(input("Digite um numero real"))
print(num1, num2, num3)
print("O produto do primeiro com metade do segundo eh : "
      , num1*(num2/2))
print("a soma do triplo do primeiro com o terceiro: ",
      (3*num1 + num3))
print("O terceiro elevado ao cubo", round(num3**3,2))
