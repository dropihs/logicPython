
"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor 
igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""


notas = []
i = 0
j = 0
acima = 0
abaixo = 0 
while i == 0: 
    notas.append(float(input("Digite uma nota (Digite -1 para parar)")))
    print("Nota digitada: ",notas[j])
    if notas[j] == -1:
        i = -1
        notas.pop(j) 
        print("Lançamento encerrado")
    j += 1
    print("Notas lançadas: ",notas)

soma = sum(notas)
media = soma/len(notas)

for i in range(len(notas)):
    if notas[i] > media: 
        acima += 1
    elif notas[i] < media: 
        abaixo += 1

print("Soma das notas: ",soma)
print("Media das notas: ",media)
print("Quantidade de notas acima da media : ",acima)
print("Quantidade de notas abaixo da media : ",abaixo)
