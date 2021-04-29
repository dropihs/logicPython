#15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# .	salário bruto.
#a.	quanto pagou ao INSS.
#b.	quanto pagou ao sindicato.
#c.	o salário líquido.
#d.	calcule os descontos e o salário líquido, conforme a tabela abaixo:
#e.	+ Salário Bruto : R$
#f.	- IR (11%) : R$
#g.	- INSS (8%) : R$
#h.	- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoHr = float(input("Digite o ganho por hora"))
hrTrab = int(input("Horas trabalhadas no mes "))
salariobruto = ganhoHr*hrTrab
ir = (ganhoHr*hrTrab)*0.11
inss = (ganhoHr*hrTrab)*0.08
sindicato = (ganhoHr*hrTrab) * 0.05
salarioliq = salariobruto-ir-inss-sindicato
print("salario bruto:  ", salariobruto)
print("ir:" , ir)
print("inss: ", inss*0.08)
print("Sindicato: ", sindicato)
print("salario liquido",salarioliq)
