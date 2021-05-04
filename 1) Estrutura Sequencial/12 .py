#12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58

altura = float(input("digite sua altura"))
pesoideal = (72.7*altura) - 58
print("Com a altura", altura, "seu peso ideal eh: ",
      round(pesoideal,2))
