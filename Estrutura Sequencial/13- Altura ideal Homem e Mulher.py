#13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# .	Para homens: (72.7*h) - 58
#a.	Para mulheres: (62.1*h) - 44.7

altura = float(input("digite sua altura"))
pesoidealhomem = (72.7*altura) - 58
pesoidealmulher = (62.1*altura) - 44.7
print("Peso ideal com a altura", altura, " homem: ",pesoidealhomem)
print("Peso ideal com a altura", altura, " mulher: ", pesoidealmulher)
