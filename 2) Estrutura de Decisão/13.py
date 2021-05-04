#13.	Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("(1)Dom(2)Seg(3)Ter(4)Quar(5)Quin(6)Sex(7)Sab")
dia = input("Digite o dia da semana: ")

if dia == '1':
    print("Domingo")

elif dia == '2': 
    print("Segunda")

elif dia == '3': 
    print("Terça")

elif dia == '4': 
    print("Quarta")

elif dia == '5': 
    print("Quinta")

elif dia == '6': 
    print("Sexta")

elif dia == '7': 
    print("Sabado")

else: 
    print("Digito errado")