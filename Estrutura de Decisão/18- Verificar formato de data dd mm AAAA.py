#18.	Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
print("{}/{}/{}".format.(dia,mes,ano)

if dia > 0 and dia <= 31:
    if mes > 0 and mes <= 12: 
        print("{}/{}/{}".format.(dia,mes,ano)

def validaData(dia, mes, ano):
    if dia > 0 and dia <= 31:
        if mes > 0 and mes <= 12:
            mostraData (str(dia), str(mes), str(ano))
        else:
            print('O mes: %s é inválido.' % (mes))
    else:
        print('O dia: %s é inválido.' % (dia))

