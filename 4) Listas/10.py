#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
import random 

vet1 = []
vet2 = []
vet3 = []

for i in range(10):
    vet1.append(random.randint(1,99))
    vet2.append(random.randint(1,99))


for i in range(20):
    
    vet3.append(vet1)
    vet3.append(vet2)

print("Primeira lista : " ,vet1)
print("Segunda lista : " ,vet2)
print("As duas listas: ", vet3)