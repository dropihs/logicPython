#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
contador = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != contador:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))
        
    lista.append(numero)
    contador += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))