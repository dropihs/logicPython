# 25.	Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  .	Álcool:
# a.	até 20 litros, desconto de 3% por litro
# b.	acima de 20 litros, desconto de 5% por litro
# c.	Gasolina:
# d.	até 20 litros, desconto de 4% por litro
# e.	acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
#       (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
#       litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
alcool = 1.90
gasolina = 2.50

c = input("(1)Alcool (2)Gasolina")

if c == '1':
    litro = float(input("Digite a quantidade de litros de Alcool: "))
    if litro <= 20: 
        preco = litro * alcool
        desconto = 3/100
    elif litro >= 21: 
        preco = litro * alcool
        desconto = 5/100
elif c == '2':
    litro = float(input("Digite a quantidade de litros de Gasolina: "))
    if litro <= 20: 
        preco = litro * gasolina
        desconto = 4/100
    elif litro >= 21: 
        preco = litro * gasolina
        desconto = 6/100   
              
valorDesconto = desconto * preco 
total = preco - valorDesconto

print("PRECO: ",preco)
print("DESCONTO: ", valorDesconto)
print("TOTAL: ", total)

#Fazer os testes dps 