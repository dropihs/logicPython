#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#resolvido com lista 


lista = []
contador = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))

while quant != contador:
    numero = lista.append(float(input("Digite um número: ")))
    contador += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))