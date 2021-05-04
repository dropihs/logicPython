#8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganhohr = float(input("Digite o ganho por hr"))
hrstrab = float(input("Hrs por dia"))
diasmes = int(input("Quantos dias vc trab no mes"))
ganho = diasmes * ganhohr * hrstrab
print(ganho)
