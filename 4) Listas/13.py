# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
# a média anual das temperaturas e mostre todas as temperaturas acima da 
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random
month = {	
        0:'Janauary',
		1:'February',
		2:'March',
		3:'April',
		4:'May',
		5:'June',
		6:'July',
		7:'August',
		8:'September',
		9:'October',
		10:'November',
		11:'December'	}
tempMes = []
for i in range(12):
    tempMes.append(random.randint(1,30))

mediaAnual = sum(tempMes)/12
print("A media anual foi: ", mediaAnual)

for i in range(12):
    print("{} - {} Temp: {}".format(i,month.get(i),tempMes[i]))
