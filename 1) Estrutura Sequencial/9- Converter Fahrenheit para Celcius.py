#9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# o	C = 5 * ((F-32) / 9).

f = float(input("Digite a temp em fahrenheit"))
celcius = 5 * ((f-32)/9)
print(f,"sao: ", round(celcius,2),"celcius")
#Round(celcius,2) serve arredondar com duas casas decimais
