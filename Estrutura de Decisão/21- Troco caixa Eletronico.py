#20.Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade
# de notas existentes na máquina.

#.	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#a.	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("====================\nCaixa Eletronico\n====================")
num = int(input("Digite o valor do saque:"))

if num <= 600 and num >= 10:
    d100 = int(num/100)
    num = num - (d100*100)

    d50 = int(num/50)
    num = num - (d50*50)

    d10 = int(num/10)
    num = num - (d10*10)

    d5 = int(num/5)
    num = num - (d5*50)

    d1 = num #Printando errado quando tem resto 

    print("Nota de 100:{}\nNota de 50:{}\nNota de 10:{}\nNota de 5:{}\nNota de 1:{}\n".format(int(d100),int(d50),int(d10),int(d5),(d1)))