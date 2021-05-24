# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
# a média anual das temperaturas e mostre todas as temperaturas acima da 
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Aug', 'Set', 'Out','Nov', 'Dez']
tempMes = []
m = [meses,tempMes]
for i in range(12):
    tempMes.append(random.randint(1,30))

mediaAnual = sum(tempMes)/12
print("A media anual foi: ", mediaAnual)
for i in range(12):
    print("{} - {} Temp: {}".format(i,meses[i],tempMes[i]))
