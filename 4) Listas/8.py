#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

arrayAltura = []
arrayIdade = []

for i in range(0,5): 
    arrayIdade.append(int(input("Digite a idade da pessoa: ", )))
    arrayAltura.append(float(input("Digite a Altura da pessoa: ", )))

print(reversed(arrayIdade))
print(reversed(arrayAltura))