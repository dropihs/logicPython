#18.	Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
import sys #para usar a funcão de dar stop 


dia = int(input("Digite o dia: "))
if (dia < 0) or (dia >= 32):
    print("Dia invalido\nEncerrando o sistema")
    sys.exit()

elif dia >= 1 and dia < 32:
    print("Dia Valido")

mes = int(input("Digite o mês: "))
if (mes < 0) or (mes >= 12):
    print("mês invalido\nEncerrando o sistema ")
    sys.exit()

elif mes > 1 and mes < 12:
    print("mês Valido")

ano = int(input("Digite o ano: "))
if ano > 0: 
    print("Ano valido")
else: 
    print("Ano invalido\nEncerrando o sistema")
    sys.exit()

print("data: {}/{}/{}".format(dia,mes,ano))