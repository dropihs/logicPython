# 9.	Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input("Primeiro Numero"))
n2 = int(input("Segundo Numero"))
n3 = int(input("Terceiro Numero"))

print("Numeros em ordem decrescente")

if n1 > n2 and n1 > n3:
    if n2 < n3:
        print(n2, n3, n1)
    elif n2 > n3:
        print(n3, n2, n1)

if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(n3, n1, n2)
    if n1 < n3:
        print(n1, n3, n2)

if n3 > n1 and n3 > n2:
    if n1 > n2:
        print(n2 , n1, n3)
    if n1 < n2:
        print(n1, n2, n3)
